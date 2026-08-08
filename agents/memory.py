import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def has_been_published(title):
    memory = load_memory()

    for item in memory:
        if item["title"] == title:
            return True

    return False


def remember_post(title, score, post):
    memory = load_memory()

    memory.append({
        "title": title,
        "score": score,
        "post": post,
        "published_at": datetime.now().isoformat()
    })

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)