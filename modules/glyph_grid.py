# glyph_grid.py — Chakra glyph grid for repeated threats

import json
import os
from collections import Counter

MEMORY_FILE = "memory/threat_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def get_top_queries(limit=6):
    memory = load_memory()
    queries = [m["Query"].lower() for m in memory]
    counter = Counter(queries).most_common(limit)
    result = []
    for q, count in counter:
        entry = next((m for m in memory if m["Query"].lower() == q), None)
        if entry:
            result.append({
                "query": q,
                "count": count,
                "intent": entry["Intent"],
                "response": entry["Response"],
                "zone": entry["Origin"]
            })
    return result
 
