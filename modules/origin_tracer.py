def trace_origin(query):
    query = query.lower()
    if "delhi" in query:
        return "Delhi, India"
    elif "pakistan" in query:
        return "Pakistan"
    elif "china" in query:
        return "China"
    elif "usa" in query or "america" in query:
        return "United States"
    elif "kashmir" in query:
        return "Kashmir Region"
    else:
        return "Unknown Origin"
