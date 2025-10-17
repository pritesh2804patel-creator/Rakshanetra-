# memory_engine.py — Stores and retrieves threat memory

import json
import os

MEMORY_FILE = "memory/threat_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(entry):
    memory = load_memory()
    memory.append(entry)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def search_memory_by_query(query):
    memory = load_memory()
    return [m for m in memory if query.lower() in m["Query"].lower()]
 
