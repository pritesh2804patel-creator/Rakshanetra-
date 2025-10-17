def detect_deception(query):
    query = query.lower()
    if any(word in query for word in ["deepfake", "fake news", "manipulated", "hoax", "rumor"]):
        return "High Deception Risk"
    elif any(word in query for word in ["anonymous", "leaked", "unverified", "uncensored"]):
        return "Moderate Deception Risk"
    else:
        return "Low Deception Risk"
