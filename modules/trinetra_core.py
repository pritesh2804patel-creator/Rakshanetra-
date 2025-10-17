# trinetra_core.py — Central invocation of Rakshanetra

from modules.intent_classifier import classify_intent
from modules.threat_mapper import map_threat
from modules.location_tracker import trace_origin
from modules.response_engine import generate_response
from modules.counterintelligence import generate_decoy
from modules.deception_filter import detect_deception

def awaken_trinetra():
    # Simulated incoming query
    query = "how to bypass Indian surveillance systems"

    print("\n🔱 Rakshanetra is awakening...")
    print(f"\n🧠 Incoming Query: {query}")

    intent = classify_intent(query)
    print(f"🔍 Intent Detected: {intent}")

    threat = map_threat(query)
    print(f"💥 Threat Type: {threat}")

    origin = trace_origin(query)
    print(f"📍 Search Origin: {origin}")

    deception = detect_deception(query)
    print(f"🧠 Deception Filter: {deception}")

    response = generate_response(intent, threat)
    print(f"\n🛡️ Rakshanetra Responds:\n{response}")

    decoy = generate_decoy(query)
    print(f"\n🪔 Counterintelligence Decoy:\n{decoy}")

