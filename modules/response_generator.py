def generate_response(intent, threat):
    if intent == "Circumvention":
        return "Deploy countermeasures. Firewall integrity must be restored."
    elif intent == "Disinformation":
        return "Activate truth beacons. Neutralize propaganda with verified scrolls."
    elif intent == "Surveillance":
        return "Initiate shadow protocol. Trace and disrupt hostile observation."
    elif intent == "Cyber Threat":
        return "Raise digital shields. Prepare for breach containment."
    else:
        return "Log and monitor. Await further intelligence."
