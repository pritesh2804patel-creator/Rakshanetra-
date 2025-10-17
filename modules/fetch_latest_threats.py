import feedparser

def fetch_latest_threats():
    rss_url = "https://news.google.com/rss/search?q=india+cyber+attack+OR+espionage+OR+vpn+OR+deepfake+OR+surveillance"
    feed = feedparser.parse(rss_url)

    if not feed or not hasattr(feed, "entries"):
        return []

    queries = []
    for entry in feed.entries[:10]:  # Limit to 10 latest
        title = entry.title if hasattr(entry, "title") else ""
        summary = entry.summary if hasattr(entry, "summary") else ""
        queries.append(f"{title} — {summary}")

    return queries
