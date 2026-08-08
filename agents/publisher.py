import json
import os
import uuid
from datetime import datetime, timezone

PUBLISHED_FILE = "published_posts.json"


def publish_post(
    title,
    post,
    score,
    rationale=None,
    sources=None
):
    published_posts = []

    if os.path.exists(PUBLISHED_FILE):
        with open(
            PUBLISHED_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            published_posts = json.load(file)

    # Generate unique post ID
    post_id = "p" + str(uuid.uuid4())[:8]

    # Current UTC time
    created_at = datetime.now(
        timezone.utc
    ).isoformat()

    # Default rationale
    if rationale is None:
        rationale = (
            "Selected because the topic is relevant "
            "to AI and technology and met the NEXUS "
            "editorial publishing standard."
        )

    # Default sources
    if sources is None:
        sources = []

    published_posts.append({
        "id": post_id,
        "title": title,
        "post": post,
        "score": score,
        "createdAt": created_at,
        "rationale": rationale,
        "sources": sources
    })

    with open(
        PUBLISHED_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            published_posts,
            file,
            indent=4,
            ensure_ascii=False
        )

    return True