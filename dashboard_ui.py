import streamlit as st
import sys
import os

# 🔧 Fix import path to access modules folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 🔗 Import Rakshanetra modules
from modules.intent_classifier import classify_intent
from modules.threat_mapper import map_threat_type
from modules.origin_tracer import trace_origin
from modules.deception_detector import detect_deception
from modules.response_generator import generate_response
from modules.decoy_generator import generate_decoy
from modules.zone_resolver import resolve_target_zone, target_zones
from modules.ip_locator import get_ip_location
from modules.visualizer import visualize_threat_map

# 🛡️ Dashboard Setup
st.set_page_config(page_title="Rakshanetra", layout="wide")
st.title("🛡️ Rakshanetra: Sovereign Threat Intelligence")

# 🔐 Ceremonial Seal
seal = st.text_input("Enter Ceremonial Seal to Access Rakshanetra")

if seal != "Jai Raksha Dharma":
    st.warning("Awaiting valid ceremonial seal...")
    st.stop()

st.success("Seal Accepted. Rakshanetra Awakens.")

# 🔍 Threat Query Input
query = st.text_area("Enter Surveillance Trigger or Threat Query")

if query:
    # 🧠 Intelligence Engines
    intent = classify_intent(query)
    threat = map_threat_type(query)
    origin = trace_origin(query)
    deception = detect_deception(query)
    response = generate_response(intent, threat)
    decoy = generate_decoy(query)
    target_coords = resolve_target_zone(query)

    # 🔒 Safety check for target_coords
    if target_coords is None:
        target_coords = [23.0, 82.0]

    # 🌍 Origin Coordinates
    ip = st.text_input("Optional: Enter Source IP")
    if ip:
        ip_data = get_ip_location(ip)
        origin_coords = [ip_data["lat"], ip_data["lon"]]
    else:
        origin_coords = [23.0, 82.0]  # Default to Central Bharat

    # 🗺️ Threat Map Visualization
    fig = visualize_threat_map(origin_coords, target_coords, query, intent, deception, target_zones)

    # 📜 Intelligence Scroll
    st.subheader("🧠 Intelligence Summary")
    st.markdown(f"""
    - **Intent**: `{intent}`
    - **Threat Type**: `{threat}`
    - **Origin**: `{origin}`
    - **Deception Risk**: `{deception}`
    - **Response**: `{response}`
    - **Decoy Protocol**: `{decoy}`
    """)

    st.subheader("🌐 Threat Map")
    st.plotly_chart(fig, use_container_width=True)
