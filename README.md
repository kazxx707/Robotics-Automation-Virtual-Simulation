# Robotics Automation & Virtual Simulation (Arduino + Python)

A minimal, interview-ready demo showing:
- **Arduino** controlling a servo-based arm sequence for pick-and-place.
- **Python** simulating the arm motion and creating a simple trajectory plot (virtual commissioning idea).

## Quick start (Python simulation)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python simulate_arm.py
```
Outputs:
- `results/motion_profile.png`
- `results/trajectory.png`

## Arduino sketch
- File: `arduino_code/arduino_code.ino`
- Uses the built-in `Servo` library.
- Plug signal to **pin 9** (changeable in code). Power servos with external 5V (shared GND).

## Talking points
- **Virtual commissioning**: validate sequences/timing and collision checks virtually before physical deployment.
- **Industry 4.0**: same control logic can be mirrored in simulation and later on the PLC/robot controller.
---

## Interview Cheat Sheet (STAR)

**Situation**: Need to automate repetitive material handling with minimal downtime.  
**Task**: Validate motion sequences and timing before deploying to hardware.  
**Action**: Implemented Arduino servo control and a Python virtual twin (2‑DOF planar model) to simulate trajectories and motion profiles; iterated on joint limits and timings safely.  
**Result**: Reduced on-floor trial-and-error; delivered reproducible plots of motion profile and end‑effector path to communicate feasibility.
