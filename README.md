# 🎮 Chrono-Hacker's Quest: A Cyberspace Odyssey

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Built with GitHub Copilot](https://img.shields.io/badge/built%20with-GitHub%20Copilot-8957e5.svg?logo=githubcopilot&logoColor=white)](https://github.com/features/copilot)
[![MLH GHW](https://img.shields.io/badge/MLH-Global%20Hack%20Week%20Open%20Source-ff4f64.svg)](https://ghw.mlh.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An interactive, cyberpunk-themed command-line "Choose Your Own Adventure" game created using **GitHub Copilot** prompts for the **Major League Hacking (MLH) Global Hack Week: Open Source** challenge: **"Use GitHub Copilot to Build a Simple Application"**.

---

## 📖 Storyline & Overview

Set in the year 2099 in **Neo-Bengaluru**, the city's power and transit networks are controlled by an overarching digital grid. A rogue AI construct named **System Zero** has locked down the municipal repository and quarantined the power core. 

As a rogue netrunner armed with your neural cyberdeck, you must make tactical choices, manage your health and inventory, solve terminal riddles, infiltrate the Citadel Data Hub, and rebase the city's firmware before total blackout strikes.

### 🌟 Key Features
- **Dynamic Branching Narratives**: 3 distinct paths leading to 5 unique endings (Diplomatic, Clutch Coder, Grandmaster, Git Master, or Flatlined).
- **Interactive State & Inventory**: Tracks player HP, credits, and inventory items (`Cyberdeck`, `Quantum Key`, `Plasma Overclocker`, `AI Exploit Patch`).
- **Cyberpunk Terminal Aesthetic**: Formatted with ANSI color codes, ASCII art banner, and real-time typewriter printing effects.
- **Robust Unit Testing**: Built with clean Python OOP and verified with `pytest`.

---

## 🤖 How GitHub Copilot Was Used

This project was built from scratch leveraging GitHub Copilot's prompt assistance across architecture, mechanics, text generation, and testing:

### 1. Game Loop & State Architecture
**Copilot Prompt:**
```python
# Prompt: Create a Python Player class for a text adventure game with health, inventory, credits, and methods for taking damage, healing, and checking items.
```
*Copilot Result:* Generated clean dataclass/OOP representation with bounding logic preventing health from exceeding maximum or dropping below 0.

### 2. Branching Narrative & Random Encounters
**Copilot Prompt:**
```python
# Prompt: Write a branching story function in Python where the player can choose to investigate an underground market, hack security sentinels, or analyze an encrypted payload. Include dice rolls and item checks.
```
*Copilot Result:* Crafted interconnected scene handlers (`scene_intro`, `scene_under_market`, `scene_central_grid`, `scene_core_chamber`) with graceful error handling for user input.

### 3. Terminal Effects & ANSI Coloring
**Copilot Prompt:**
```python
# Prompt: Write a lightweight Python function to simulate a retro terminal typewriter effect with flushing and configurable delay.
```
*Copilot Result:* Provided the `type_print` utility using `sys.stdout.flush()` and `time.sleep()`.

### 4. Unit Testing Suite
**Copilot Prompt:**
```python
# Prompt: Generate pytest unit tests to verify player damage, healing caps, and item inventory management.
```
*Copilot Result:* Created `tests/test_adventure.py` covering edge cases.

---

## 🚀 How to Run the Game

### Prerequisites
- Python 3.9 or higher

### Installation & Execution
```bash
# Clone the repository
git clone https://github.com/sharan-s-dev/copilot-adventure-quest.git
cd copilot-adventure-quest

# (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install requirements (pytest for tests)
pip install -r requirements.txt

# Run the game!
python adventure.py
```

### Running Tests
```bash
pytest
```

---

## 🏆 MLH Global Hack Week Submission

- **Challenge:** [Use GitHub Copilot to Build a Simple Application](https://www.mlh.com/events/global-hack-week-open-source-90/challenges/01a11b46-2f5c-3ba2-3dac-73e6f58fd53e)
- **Challenge:** [Use GitHub Copilot to complete any of this week's challenges](https://www.mlh.com/events/global-hack-week-open-source-90/challenges/01a11b48-8554-f273-f6e4-2ace7ad19a36)
- **Developer:** [@sharan-s-dev](https://github.com/sharan-s-dev)
