# pattern_detector.py — Detects repeated threats and zones

import json
from collections import Counter
import os

MEMORY_FILE = "memory/threat_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def detect_repeated_queries():
    memory = load_memory()
    queries = [m["Query"].lower() for m in memory]
    return Counter(queries).most_common(5)

def detect_targeted_zones():
    memory = load_memory()
    zones = []
    for m in memory:
        for zone in ["gujarat", "delhi", "kashmir", "mumbai", "chennai"]:
            if zone in m["Query"].lower():
                zones.append(zone)
    return Counter(zones).most_common(5)
 
