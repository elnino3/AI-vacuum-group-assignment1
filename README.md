# Vacuum Cleaner Simulation – Table-Driven Agent

## Description
This project simulates a simple **AI vacuum cleaner agent** HARD LEVEL operating in a two-room environment.  
The agent uses a **table-driven reflex model** to decide actions based on its current percept (room status + location).  
An additional background thread (`evilMan`) continuously dirties the environment, simulating a dynamic adversarial world.

---

## Features
- Two-room environment (`A` and `B`)
- Agent actions: `MoveLeft`, `MoveRight`, `Suck`
- Background thread that dirties rooms
- 10-step simulation loop with printed outputs

---

## Requirements
- Python 3.x
- Standard libraries: `threading`, `time`, `random`

---

## Usage
Run the program directly:

```bash
python vacuum_simulation.py
