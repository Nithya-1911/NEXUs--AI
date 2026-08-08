import time

from agents.discover import discover_topics
from agents.evaluator import evaluate_topic
from agents.writer import write_post
from agents.memory import has_been_published, remember_post
from agents.publisher import publish_post


def run_nexus():

    print("\n🔎 Discovering new topics...")

    topics = discover_topics()

    for topic in topics:

        title = topic["title"]

        print(f"\n📰 Topic: {title}")

        # -----------------------------
        # Evaluate topic
        # -----------------------------

        score = evaluate_topic(topic)

        print(f"📊 Score: {score}")

        # -----------------------------
        # Reject low-score topics
        # -----------------------------

        if score < 5:

            print("⏭️ Skipped: score too low")

            continue

        # -----------------------------
        # Check memory
        # -----------------------------

        if has_been_published(title):

            print("🧠 Skipped: already published")

            continue

        # -----------------------------
        # Generate post
        # -----------------------------

        post = write_post(
            title,
            topic["summary"],
            score
        )

        # -----------------------------
        # Publishing rationale
        # -----------------------------

        rationale = (
            f"Selected because this topic received "
            f"a NEXUS score of {score} and is relevant "
            f"to AI and technology."
        )

        # -----------------------------
        # Source URL
        # -----------------------------

        source = topic.get("link", "")

        sources = []

        if source:
            sources.append(source)

        # -----------------------------
        # Save published post
        # -----------------------------

        publish_post(
            title,
            post,
            score,
            rationale,
            sources
        )

        # -----------------------------
        # Remember published topic
        # -----------------------------

        remember_post(
            title,
            score,
            post
        )

        print("✍️ Post created")
        print("📤 Post saved")
        print("✅ Topic completed")


# -----------------------------
# Autonomous operation
# -----------------------------

if __name__ == "__main__":

    print("\n🚀 NEXUS Autonomous Agent Started")

    while True:

        run_nexus()

        print("\n⏳ Waiting 5 minutes before next cycle...")

        time.sleep(300)