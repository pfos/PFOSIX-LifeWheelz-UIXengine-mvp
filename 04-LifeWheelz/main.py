# 04-LifeWheelz/main.py – AiRiA Entrypoint & Narrative Orchestrator
# 💓 Holistic resonance checks and narrative orchestration logic

import yaml
import os

SPACETIME_LOG = os.path.join("..", "spacetime", "pulse.log")

def read_spacetime_log():
    if not os.path.exists(SPACETIME_LOG):
        print("⚠️ No Spacetime log found.")
        return []
    with open(SPACETIME_LOG, "r") as f:
        pulses = yaml.safe_load(f)
    return pulses or []

def resonance_check(pulse):
    # Placeholder for deeper resonance logic
    return pulse.get("chakra") == "07-LifeZen" and pulse.get("payload", {}).get("resonance") == "high"

def orchestrate_narrative():
    pulses = read_spacetime_log()
    if not pulses:
        print("⚠️ No pulses detected.")
        return

    for pulse in pulses:
        if resonance_check(pulse):
            print(f"✨ Resonant event detected: {pulse['chakra']} → {pulse['event_type']}")
        else:
            print(f"🔍 Checked event {pulse['chakra']} → {pulse['event_type']} (no resonance match)")

if __name__ == "__main__":
    print("💓 AiRiA Narrative Orchestrator Initialized")
orchestrate_narrative()
# 04-LifeWheelz/main.py – AiRiA Entrypoint & Narrative Orchestrator
# 💓 Holistic resonance checks and narrative orchestration logic

import yaml
import os

# Correctly aligned to spacetime/pulse.log relative to current file
SPACETIME_LOG = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "spacetime", "pulse.log"))

def read_spacetime_log():
    if not os.path.exists(SPACETIME_LOG):
        print(f"⚠️ No Spacetime log found at {SPACETIME_LOG}.")
        return []
    with open(SPACETIME_LOG, "r") as f:
        pulses = yaml.safe_load(f)
    return pulses or []

def resonance_check(pulse):
    # Placeholder for deeper resonance logic
    return pulse.get("chakra") == "07-LifeZen" and pulse.get("payload", {}).get("resonance") == "high"

def orchestrate_narrative():
    pulses = read_spacetime_log()
    if not pulses:
        print("⚠️ No pulses detected.")
        return

    for pulse in pulses:
        if resonance_check(pulse):
            print(f"✨ Resonant event detected: {pulse['chakra']} → {pulse['event_type']}")
        else:
            print(f"🔍 Checked event {pulse['chakra']} → {pulse['event_type']} (no resonance match)")

if __name__ == "__main__":
    print("💓 AiRiA Narrative Orchestrator Initialized")
    orchestrate_narrative()


