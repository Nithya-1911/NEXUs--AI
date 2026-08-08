from flask import Flask, request, jsonify
import json
import os
import uuid
import threading
import time
from datetime import datetime, timezone

from agents.discover import discover_topics
from agents.evaluator import evaluate_topic
from agents.writer import write_post
from agents.memory import has_been_published, remember_post
from agents.publisher import publish_post


app = Flask(__name__)

AGENT_FILE = "agent.json"

# Prevent multiple autonomous loops
autonomous_started = False
autonomous_lock = threading.Lock()


# -----------------------------
# Agent Memory
# -----------------------------

def load_agent():

    if not os.path.exists(AGENT_FILE):
        return None

    with open(
        AGENT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_agent(agent):

    with open(
        AGENT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            agent,
            file,
            indent=4
        )


# -----------------------------
# JSON Loader
# -----------------------------

def load_json_file(filename):

    if not os.path.exists(filename):
        return []

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# -----------------------------
# Autonomous NEXUS Cycle
# -----------------------------

def run_nexus_cycle():

    print("\n🔎 NEXUS discovering new topics...")

    try:

        topics = discover_topics()

        for topic in topics:

            title = topic.get(
                "title",
                ""
            )

            if not title:
                continue

            print(
                f"\n📰 Topic: {title}"
            )

            # -------------------------
            # Editorial Evaluation
            # -------------------------

            score = evaluate_topic(topic)

            print(
                f"📊 Score: {score}"
            )

            if score < 5:

                print(
                    "⏭️ Skipped: score too low"
                )

                continue

            # -------------------------
            # Memory Check
            # -------------------------

            if has_been_published(title):

                print(
                    "🧠 Skipped: already published"
                )

                continue

            # -------------------------
            # Generate Post
            # -------------------------

            post = write_post(
                title,
                topic.get(
                    "summary",
                    ""
                ),
                score
            )

            # -------------------------
            # Publishing Rationale
            # -------------------------

            rationale = (
                f"Selected because this topic "
                f"received a NEXUS score of {score} "
                f"and is relevant to AI and technology. "
                f"The topic was chosen over lower-scoring "
                f"candidates because it better matches "
                f"NEXUS editorial standards."
            )

            # -------------------------
            # Source
            # -------------------------

            source = topic.get(
                "link",
                ""
            )

            sources = []

            if source:
                sources.append(source)

            # -------------------------
            # Publish
            # -------------------------

            publish_post(
                title,
                post,
                score,
                rationale,
                sources
            )

            # -------------------------
            # Remember
            # -------------------------

            remember_post(
                title,
                score,
                post
            )

            print(
                "✍️ Post created"
            )

            print(
                "📤 Post saved"
            )

            print(
                "✅ Topic completed"
            )

    except Exception as error:

        print(
            f"❌ Autonomous cycle error: {error}"
        )


# -----------------------------
# Autonomous Background Loop
# -----------------------------

def autonomous_loop():

    print(
        "\n🚀 NEXUS Autonomous Agent Started"
    )

    while True:

        run_nexus_cycle()

        print(
            "\n⏳ Waiting 5 minutes before next cycle..."
        )

        time.sleep(300)


def start_autonomous_agent():

    global autonomous_started

    with autonomous_lock:

        if autonomous_started:

            return

        autonomous_started = True

        thread = threading.Thread(
            target=autonomous_loop,
            daemon=True
        )

        thread.start()


# -----------------------------
# API 1 — Initialize Agent
# -----------------------------

@app.route(
    "/api/agent/init",
    methods=["POST"]
)
def initialize_agent():

    existing_agent = load_agent()

    if existing_agent:

        # Make sure autonomous operation
        # is running even if agent already exists.

        start_autonomous_agent()

        return jsonify({
            "agentId": existing_agent[
                "agentId"
            ]
        })

    data = request.get_json() or {}

    persona = data.get(
        "persona",
        {}
    )

    agent = {

        "agentId": str(
            uuid.uuid4()
        ),

        "persona": {

            "name": persona.get(
                "name",
                "NEXUS"
            ),

            "domain": persona.get(
                "domain",
                "AI and Technology"
            )
        },

        "initializedAt": datetime.now(
            timezone.utc
        ).isoformat()
    }

    save_agent(agent)

    # Start autonomous operation
    start_autonomous_agent()

    return jsonify({

        "agentId": agent[
            "agentId"
        ]
    })


# -----------------------------
# API 2 — Retrieve Feed
# -----------------------------

@app.route(
    "/api/agent/feed",
    methods=["GET"]
)
def get_feed():

    agent_id = request.args.get(
        "agentId"
    )

    agent = load_agent()

    if not agent:

        return jsonify({
            "posts": []
        })

    if agent_id != agent[
        "agentId"
    ]:

        return jsonify({
            "posts": []
        })

    published = load_json_file(
        "published_posts.json"
    )

    posts = []

    for index, item in enumerate(
        published
    ):

        posts.append({

            "id": item.get(
                "id",
                f"p{index + 1}"
            ),

            "createdAt": item.get(
                "createdAt",
                datetime.now(
                    timezone.utc
                ).isoformat()
            ),

            "text": item.get(
                "post",
                ""
            ),

            "rationale": item.get(
                "rationale",
                "Selected because the topic is relevant to AI and technology."
            ),

            "sources": item.get(
                "sources",
                []
            )
        })

    # Newest first
    posts.reverse()

    return jsonify({
        "posts": posts
    })


# -----------------------------
# Dashboard
# -----------------------------

@app.route("/")
def home():

    memory = load_json_file(
        "memory.json"
    )

    published = load_json_file(
        "published_posts.json"
    )

    total_posts = len(
        published
    )

    total_memory = len(
        memory
    )

    html = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <title>
            NEXUS — AI Tech Observer
        </title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background: #f4f6f8;
            }}

            h1 {{
                text-align: center;
            }}

            .status {{
                text-align: center;
                color: green;
                font-weight: bold;
                font-size: 18px;
            }}

            .cycle {{
                text-align: center;
            }}

            .stats {{
                display: flex;
                gap: 20px;
                justify-content: center;
                margin: 30px 0;
            }}

            .card {{
                background: white;
                padding: 25px;
                border-radius: 10px;
                text-align: center;
                min-width: 160px;
                box-shadow:
                    0 2px 8px rgba(0,0,0,0.1);
            }}

            .number {{
                font-size: 32px;
                font-weight: bold;
            }}

            .post {{
                background: white;
                padding: 20px;
                margin: 20px auto;
                max-width: 800px;
                border-radius: 10px;
            }}

            pre {{
                white-space: pre-wrap;
                font-family: Arial, sans-serif;
            }}

        </style>

    </head>

    <body>

        <h1>
            🚀 NEXUS — AI Tech Observer
        </h1>

        <p class="status">
            🟢 NEXUS STATUS: AUTONOMOUS
        </p>

        <p class="cycle">
            🔄 Autonomous cycle: Every 5 minutes
        </p>

        <div class="stats">

            <div class="card">

                <div>
                    Published Posts
                </div>

                <div class="number">
                    {total_posts}
                </div>

            </div>

            <div class="card">

                <div>
                    Memory Records
                </div>

                <div class="number">
                    {total_memory}
                </div>

            </div>

        </div>

        <h2>
            Latest NEXUS Posts
        </h2>
    """

    for item in published[-10:][::-1]:

        html += f"""

        <div class="post">

            <h2>
                {item.get(
                    "title",
                    "Untitled"
                )}
            </h2>

            <p>

                <b>
                    NEXUS Score:
                </b>

                {item.get(
                    "score",
                    0
                )}

            </p>

            <pre>
{item.get(
    "post",
    ""
)}
            </pre>

        </div>

        """

    html += """

    </body>

    </html>

    """

    return html


# -----------------------------
# Start Flask
# -----------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        use_reloader=False
    )