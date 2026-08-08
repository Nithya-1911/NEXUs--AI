import feedparser


def discover_topics():

    feeds = [
        "https://techcrunch.com/feed/",
        "https://www.theverge.com/rss/index.xml"
    ]

    topics = []

    for feed_url in feeds:

        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:5]:

            topics.append({
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", "")
            })

    return topics