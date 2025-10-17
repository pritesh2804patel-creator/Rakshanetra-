target_zones = { 
    "north": [30.0, 78.0], 
    "south": [10.0, 78.0], 
    "east": [25.0, 88.0], 
    "west": [22.0, 72.0], 
    "central": [23.0, 82.0], 
    "kashmir": [34.0, 74.0], 
    "northeast": [27.0, 94.0] 
} 
 
def resolve_target_zone(query):
    query = query.lower()
    for zone in target_zones:
        if zone in query:
            return target_zones[zone]
    return [23.0, 82.0]  # Default to central Bharat
