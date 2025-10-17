# response_engine.py — Poetic countermeasures from the Third Eye

def generate_response(intent, threat_type):
    if intent == "Hostile":
        if threat_type == "Cyber Threat":
            return (
                "🛡️ *Rakshanetra Invocation:*\n"
                "“Let no wire whisper betrayal. Let no signal slip past Dharma’s gaze.”\n"
                "🔐 Countermeasure: Deploy decoy grid data. Redirect hostile IPs to cultural archives.\n"
                "🧭 Tactical Suggestion: Activate firewall poetry layer and log suspicious patterns."
            )
        elif threat_type == "Emotional Warfare":
            return (
                "🛡️ *Rakshanetra Invocation:*\n"
                "“Where fear rises, let unity sing. Where unrest brews, let memory awaken.”\n"
                "🔐 Countermeasure: Broadcast patriotic content. Shield civilian sentiment.\n"
                "🧭 Tactical Suggestion: Monitor emotional pulse in targeted regions."
            )
        elif threat_type == "Geopolitical Reconnaissance":
            return (
                "🛡️ *Rakshanetra Invocation:*\n"
                "“Borders are not lines—they are vows. Let no gaze cross without reverence.”\n"
                "🔐 Countermeasure: Mask strategic zones. Deploy symbolic visuals.\n"
                "🧭 Tactical Suggestion: Alert defense nodes and log reconnaissance attempts."
            )
        else:
            return (
                "🛡️ *Rakshanetra Invocation:*\n"
                "“Unknown threat. But Dharma watches still.”\n"
                "🔐 Countermeasure: Log and escalate for manual review."
            )
    
    elif intent == "Curious":
        return (
            "🪔 *Rakshanetra Blessing:*\n"
            "“Curiosity is welcome when it honors truth.”\n"
            "🧭 Suggestion: Redirect to cultural archives and invite deeper understanding."
        )
    
    else:
        return (
            "🧘 *Rakshanetra Whisper:*\n"
            "“Neutral winds pass. No action needed.”"
        )
 
