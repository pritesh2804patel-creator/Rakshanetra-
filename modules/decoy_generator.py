def generate_decoy(query):
    query = query.lower()
    if any(word in query for word in ["vpn", "proxy", "mask", "cloak"]):
        return "Deploy Phantom Gateway"
    elif any(word in query for word in ["fake news", "rumor", "hoax"]):
        return "Release Truth Mirage"
    elif any(word in query for word in ["spy", "surveillance", "espionage"]):
        return "Activate Shadow Pulse"
    elif any(word in query for word in ["attack", "bomb", "weapon", "hack"]):
        return "Trigger Firewall Bloom"
    else:
        return "Echo Silence Protocol"
