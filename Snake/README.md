# 🐍 Retro Snake Game

A classic, object-oriented 2D Snake game built entirely in pure Python using the native `turtle` graphics library. The project leverages structured design patterns to cleanly separate game logic, rendering, entity state, and real-time score keeping.

---

## ✨ Features

* **Object-Oriented Design:** Modular codebase broken into distinct, maintainable classes (`Snake`, `Food`, `Scoreboard`).
* **Dynamic Screen-Edge Scaling:** Automatically maps pixel boundaries based on responsive real-time window calculations instead of fragile, hardcoded values.
* **Intelligent Entity Placement:** Features a validation loop tracking segment coordinates to prevent food targets from ever spawning invisibly underneath the snake's body.
* **Frame-Locked Keystroke Buffer:** Prevents instant self-collision crashes caused by pressing multiple turn keys faster than a single loop tick.
* **Scaling Difficulty Engine:** Automatically speeds up frame loops incrementally as your score rises to continuously increase game difficulty.
* **Frame-Rate Smoothness:** Implements double-buffering via screen tracer overrides (`screen.tracer(0)`) to eliminate graphic flickering during movement.

---

## 🏗️ Architecture & File Breakdown

The application is structured cleanly across four core components:

* **`main.py`**: The game engine orchestrating the central loop, timing, screen scaling, boundary collision checks, and keyboard event listening.
* **`snake.py`**: Controls segment array instantiations, spatial tracking, forward vector translation, and directional heading state blocks.
* **`food.py`**: Inherits from the native `Turtle` class to manage color randomization and overlapping coordinate verification safety checks.
* **`scoreboard.py`**: Anchors data persistence for real-time tracking, clearing, and refreshing score strings cleanly across upscaled game windows.

---

## 🛠️ Prerequisites & Installation

### Required Environment
* **Runtime:** Python (v3.8+)
* **Dependencies:** None. Uses Python Standard Library components (`turtle`, `time`, `random`).

### Quick Start (Sparse Checkout)
To download and extract only the Snake game directory without pulling down the entire multi-project repository workspace, execute the following commands in your terminal:

```bash
# 1. Initialize an empty local repository
mkdir snake && cd snake
git init

# 2. Add your multi-project repo as the remote origin
git remote add origin https://github.com/sergio-a-juarez-1/Python-Projects.git

# 3. Enable sparse-checkout and tell Git exactly which folder you want
git sparse-checkout set Snake

# 4. Pull down only that folder's files
git pull origin main

# 5. Navigate into the game directory and run
cd Snake
python3 main.py
```

---

## 🎮 Controls & Gameplay Mechanics

Interact with the interface using standard directional keyboard mapping:

* **`Up Arrow`**: Pivot heading upward (Locked out if heading downward or if turn buffer is locked for the frame).
* **`Down Arrow`**: Pivot heading downward (Locked out if heading upward or if turn buffer is locked for the frame).
* **`Left Arrow`**: Pivot heading leftward (Locked out if heading rightward or if turn buffer is locked for the frame).
* **`Right Arrow`**: Pivot heading rightward (Locked out if leading leftward or if turn buffer is locked for the frame).

### Rules
* Consuming a turtle target expands the snake body length, resets a safe target position, and increases score by +1.
* Striking any outer screen boundary calculated relative to window proportions triggers an instant Game Over.
* Colliding with any trailing segments within the body array triggers an instant Game Over.

