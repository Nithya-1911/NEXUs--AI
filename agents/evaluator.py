def evaluate_topic(topic):

    title = topic["title"].lower()
    summary = topic["summary"].lower()

    score = 0

    # AI relevance
    ai_keywords = [
        "ai",
        "artificial intelligence",
        "machine learning",
        "openai",
        "anthropic",
        "google",
        "microsoft",
        "robot",
        "robotics",
        "model"
    ]

    for keyword in ai_keywords:
        if keyword in title or keyword in summary:
            score += 5
            break

    # Technology relevance
    tech_keywords = [
        "technology",
        "software",
        "chip",
        "computer",
        "cloud",
        "cybersecurity",
        "data",
        "startup"
    ]

    for keyword in tech_keywords:
        if keyword in title or keyword in summary:
            score += 3
            break

    # News importance
    important_keywords = [
        "launch",
        "released",
        "announces",
        "new",
        "update",
        "breakthrough",
        "security",
        "acquisition"
    ]

    for keyword in important_keywords:
        if keyword in title or keyword in summary:
            score += 2
            break

    return score