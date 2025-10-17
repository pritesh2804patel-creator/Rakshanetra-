# location_tracker.py — Tracing the shadow’s origin

def trace_origin(query):
    # Simulated logic: infer origin based on keywords
    foreign_keywords = ["bypass", "exploit", "hack", "surveillance"]
    regional_keywords = ["border", "PMO", "army", "civilian"]

    query_lower = query.lower()

    if any(word in query_lower for word in foreign_keywords):
        return "Foreign IP Cluster (Suspicious)"
    elif any(word in query_lower for word in regional_keywords):
        return "Targeting Bharat’s Strategic Zones"
    else:
        return "Origin Unknown"
 
