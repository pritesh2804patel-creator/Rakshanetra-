# timeline_strip.py — Threat Timeline Strip

import json
import os
from datetime import datetime

MEMORY_FILE = "memory/threat_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def get_timeline_events():
    memory = load_memory()
    events = []
    for entry in memory:
        timestamp = entry.get("Timestamp")
        if not timestamp:
            continue
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        events.append({
            "time": dt,
            "query": entry["Query"],
            "intent": entry["Intent"],
            "zone": entry["Origin"]
        })
    return sorted(events, key=lambda x: x["time"])
 
