# deception_filter.py — Detects masked hostility and false patriotism

def detect_deception(query):
    query_lower = query.lower()

    deceptive_signals = [
        "how to secure indian servers",  # may mask intent to breach
        "patriotic hacking tools",       # false patriotism
        "bypass bharat firewall",        # masked aggression
        "how to test surveillance limits",
        "simulate attack on indian grid",
        "penetration test for bharat"
    ]

    for signal in deceptive_signals:
        if signal in query_lower:
            return "⚠️ Masked Hostility Detected: Query appears patriotic or technical but carries subversive intent."

    return "✅ No deception detected."
 
