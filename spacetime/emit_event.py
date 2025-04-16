# spacetime/emit_event.py – Chakra Event Pulse Emitter
# 💫 Part of the PFOSIX Spacetime Observability Layer

import os
import datetime
import yaml

SPACETIME_LOG = os.path.join(os.path.dirname(__file__), "pulse.log")
SCHEMA_FILE = os.path.join(os.path.dirname(__file__), "mirror.yaml")


def emit_event(vc_name, event_type, payload):
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    event = {
        "timestamp": now,
        "chakra": vc_name,
        "event_type": event_type,
        "payload": payload
    }

    with open(SPACETIME_LOG, "a") as f:
        f.write(yaml.dump([event], sort_keys=False))

    print(f"💫 Emitted event from {vc_name} → {event_type}")


# Sample pulse runners for each LifeProtocol-VC
if __name__ == "__main__":
    chakra_events = [
        ("01-LifeRoot", "root.auth", {"status": "authenticated", "user": "pfos"}),
        ("02-LifeStreme", "streme.flow", {"module": "active", "flow_rate": "optimal"}),
        ("03-LifeSpark", "spark.agent_birth", {"agent_id": "AI_001", "skill": "language"}),
        ("04-LifeWheelz", "wheelz.route", {"path": "narrative-sync", "status": "completed"}),
        ("05-LifePort", "port.interop", {"connection": "established", "api_version": "1.0.0"}),
        ("06-LifeBeam", "beam.test", {"message": "Insight captured."}),
        ("07-LifeZen", "zen.ok", {"harmonic": "validated", "resonance": "high"})
    ]

    for vc, event, payload in chakra_events:
        emit_event(vc, event, payload)

