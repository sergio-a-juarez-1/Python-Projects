# 🐍 Retro Snake Game

A classic, object-oriented 2D Snake game built entirely in pure Python using the native `turtle` graphics library. The project leverages structured design patterns to cleanly separate game logic, rendering, entity state, and real-time score keeping.

---

## ✨ Features

* **Object-Oriented Design:** Modular codebase broken into distinct, maintainable classes (`Snake`, `Food`, `Scoreboard`).
* **Dynamic Entity Customization:** The snake features a distinct directional arrow head, while food targets automatically cycle through randomized vibrant colors on every respawn.
* **Frame-Rate Smoothness:** Implements double-buffering via screen tracer overrides (`screen.tracer(0)`) to eliminate graphic flickering during movement.
* **Accurate Collision Physics:** Programmed bounding-box detection handling wall impacts and precise self-cannibalism (tail collision) rules.

---

## 🏗️ Architecture & File Breakdown

The application is structured cleanly across four core components:

* **`main.py`**: The game engine orchestrating the central loop, timing, window configuration, and keyboard event listening.
* **`snake.py`**: Controls segment array instantiations, spatial tracking, forward vector translation, and directional heading constraints.
* **`food.py`**: Inherits from the native `Turtle` class to manage random spatial distribution (`randint`) and aesthetic color logic.
* **`scoreboard.py`**: Anchors data persistence for real-time tracking, clearing, and refreshing score strings on screen.

---

## 🛠️ Prerequisites & Installation

### Required Environment
* **Runtime:** Python (v3.8+)
* **Dependencies:** None. Uses Python Standard Library components (`turtle`, `time`, `random`).

### Quick Start
1. Clone your project directory or copy the source files into a unified folder.
2. Launch the application terminal execution:
```bash
python main.py
```

---

## 🎮 Controls & Gameplay Mechanics

Interact with the interface using standard directional keyboard mapping:

* **`Up Arrow`**: Pivot heading upward (Locked out if heading downward).
* **`Down Arrow`**: Pivot heading downward (Locked out if heading upward).
* **`Left Arrow`**: Pivot heading leftward (Locked out if heading rightward).
* **`Right Arrow`**: Pivot heading rightward (Locked out if heading leftward).

### Rules
* Consuming a turtle target expands the snake body length and increases your core score by +1.
* Striking any outer screen boundary ($X/Y \ge \pm290$) triggers an instant Game Over.
* Colliding with any trailing segments within the body array triggers an instant Game Over.
Use code with caution.Would you like to expand this with an added section explaining how the coordinate grid system handles the screen limits, or instructions on implementing a persistent High Score tracking system?
