# Creative Intent Agent (FIBO Hackathon)
# Part 2 — Agent Logic (No external APIs yet)

import json

# -----------------------------
# STEP 1: Input Creative Brief
# -----------------------------

creative_brief = """
The campaign should position the brand as premium yet approachable, with a modern editorial sensibility.
Visuals should feel warm and human, while maintaining a clean, elevated look suitable for a national rollout.
The product must be the hero and clearly recognizable, but should not feel overly staged or artificial.

We are aiming for a look that feels intimate and authentic, but also scalable across paid digital, OOH,
and retail displays. Talent should feel diverse and relatable.
Lighting should feel natural and honest, though still polished enough to meet brand standards.

Please avoid anything that could raise regulatory or claims concerns.
Budget is limited, so the execution should feel efficient,
but the final output must not look cost-conscious.
"""

print("\n--- CREATIVE BRIEF ---")
print(creative_brief)

# -----------------------------
# STEP 2: Agent Asks Questions
# -----------------------------

print("\n--- AGENT CLARIFYING QUESTIONS ---")

q1 = input("1) Should this feel intimate or aspirational? ")
q2 = input("2) Is the camera meant to observe the subject or feel close and personal? ")
q3 = input("3) Do you want warmer tones or neutral tones? ")

# -----------------------------
# STEP 3: Translate to FIBO JSON
# -----------------------------

fibo_json = {
    "camera": {
        "angle": "eye_level",
        "distance": "medium_close",
        "field_of_view": "standard"
    },
    "lighting": {
        "style": "natural_diffused",
        "contrast": "low",
        "mood": "soft_realistic"
    },
    "color": {
        "palette": "warm_neutrals",
        "temperature": "slightly_warm",
        "saturation": "muted"
    },
    "composition": {
        "subject_priority": "product_hero",
        "framing": "center_weighted",
        "negative_space": "moderate"
    },
    "intent_layer": {
        "emotional_tone": q1,
        "camera_relationship": q2,
        "color_preference": q3
    }    ,
    "production_safety_layer": {
        "detected_risks": [
            "Premium visual expectations paired with limited budget",
            "Multi-channel deployment requested without format-specific guidance",
            "Regulatory sensitivity mentioned without explicit claims boundaries"
        ],
        "resolution_strategy": {
            "lighting_decision": "natural_diffused lighting chosen to minimize production complexity while maintaining premium feel",
            "composition_decision": "center_weighted framing selected to allow safe cropping across OOH, digital, and retail formats",
            "color_decision": "muted neutral palette applied to avoid exaggerated visual claims"
        },
        "confidence_level": "production_safe"
    }

}


print("\n--- GENERATED FIBO-READY JSON ---")
print(json.dumps(fibo_json, indent=2))

# -----------------------------
# END
# -----------------------------
