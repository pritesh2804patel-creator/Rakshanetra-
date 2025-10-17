# placeholder 

def classify_intent(query):
    query = query.lower()
    if any(word in query for word in ["bypass", "vpn", "proxy", "firewall"]):
        return "Circumvention"
    elif any(word in query for word in ["fake news", "propaganda", "manipulate"]):
        return "Disinformation"
    elif any(word in query for word in ["spy", "surveillance", "espionage"]):
        return "Surveillance"
    elif any(word in query for word in ["attack", "bomb", "weapon", "hack"]):
        return "Cyber Threat"
    else:
        return "Unknown"
