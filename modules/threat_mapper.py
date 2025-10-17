def map_threat_type(query):
    query = query.lower()
    if any(word in query for word in ["vpn", "proxy", "bypass", "circumvent"]):
        return "Circumvention"
    elif any(word in query for word in ["fake news", "rumor", "deepfake", "hoax"]):
        return "Disinformation"
    elif any(word in query for word in ["spy", "surveillance", "espionage", "tracking"]):
        return "Surveillance"
    elif any(word in query for word in ["attack", "bomb", "weapon", "malware", "hack"]):
        return "Cyber Threat"
    else:
        return "Unclassified"
