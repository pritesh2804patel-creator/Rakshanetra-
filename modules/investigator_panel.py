# investigator_panel.py — Daily Ritual Briefing

import json
import os
from collections import Counter

MEMORY_FILE = "memory/threat_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def get_daily_briefing():
    memory = load_memory()
    if not memory:
        return {}

    queries = [m["Query"].lower() for m in memory]
    zones = [m["Origin"] for m in memory]
    decoys = [m["Decoy"] for m in memory]
    deceptions = sorted(memory, key=lambda x: len(x["Deception"]), reverse=True)

    return {
        "most_deceptive": deceptions[0]["Query"] if deceptions else None,
        "most_repeated": Counter(queries).most_common(1)[0][0] if queries else None,
        "most_targeted_zone": Counter(zones).most_common(1)[0][0] if zones else None,
        "most_used_decoy": Counter(decoys).most_common(1)[0][0] if decoys else None
    }
 
