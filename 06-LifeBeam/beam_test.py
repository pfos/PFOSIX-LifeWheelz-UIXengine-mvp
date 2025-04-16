# beam_test.py – Test event emitter from LifeBeam VC
import sys
import os

# Precisely set the path to the spacetime directory
current_dir = os.path.dirname(os.path.abspath(__file__))
spacetime_dir = os.path.abspath(os.path.join(current_dir, "..", "spacetime"))
sys.path.append(spacetime_dir)

from emit_event import emit_event

emit_event("06-LifeBeam", "beam.test", {"message": "I see the pattern clearly."})

