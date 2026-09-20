# 🍅 Tkinter Pomodoro Timer

A slick, desktop-based productivity application built in Python using the `tkinter` GUI framework. The app implements the classic **Pomodoro Technique**—cycling through focused work sessions punctuated by short and long breaks.

---

## 🛠️ Refactored Architecture & Efficiency Updates

This updated version stabilizes background loop behaviors and fixes environment vulnerabilities found in legacy implementations:

*   **Multi-Trigger Lockout (`is_running`):** Implements a state-tracking toggle preventing users from creating stacking overlay loops by clicking "Start" repeatedly.
*   **Dynamic OS Path Mapping:** Drops hardcoded system absolute lookups in favor of safe relative workspace indexing (`os.path.join`), preventing file-not-found system breaks.
*   **Asset Fault Tolerance:** Built-in structural try-except fallback draws a procedural geometric canvas tomato vector layout if the binary source `.png` asset is unavailable.
*   **Clean String Conversions:** Replaced standard manual condition parsing with native zero-padded format expressions (`:02d`) within timer elements.

---

## 🚀 Features

*   **Classic Interval Flow**: Automatic cycling between 25-minute work rounds, 5-minute short breaks, and a 20-minute long break after 4 rounds.
*   **Visual Status Indicator**: Distinct layout color themes instantly signal your current state (Work 🟢, Short Break 💗, Long Break 🔴).
*   **Dynamic Milestones**: Automatically tracks your progress visually by displaying checkmarks (✓) for every completed work block.
*   **Zero Dependencies**: Relies solely on Python's built-in libraries.

---

## 🛠️ Getting Started & Installation

### 1. Prerequisites
Ensure you have **Python 3.10+** installed. Tkinter typically comes pre-installed with standard Python distributions.

If you are on a Linux distribution and missing Tkinter, install it via your package manager:
```bash
sudo apt-get install python3-tk
```

### 2. Isolate the Project (Sparse-Checkout)
If you only want to download this specific tool without pulling down the entire `Python-Projects` monorepo, follow these steps to initialize a targeted local repository:

```bash
# 1. Initialize an empty local repository
mkdir pomodoro-app && cd pomodoro-app
git init

# 2. Add your multi-project repo as the remote origin
git remote add origin https://github.com/sergio-a-juarez-1/Python-Projects.git

# 3. Enable sparse-checkout and tell Git exactly which folder you want
git sparse-checkout set Pomodoro

# 4. Pull down only that folder's files
git pull origin main
```

---

## 💻 Usage

Navigate into your isolated project directory and fire up the application terminal instance:

```bash
cd Pomodoro
python main.py
```

### App Mechanics
*   **Start**: Kicks off the timer countdown mechanism. The lockout engine blocks rapid, accidental button presses.
*   **Reset**: Instantly flushes internal session counts back to zero, clears checks, and halts active clock cycles.

---

## ⚙️ Configuration Constants

You can easily adjust the cycle times directly near the top of `main.py`:

```python
# Values are calculated in seconds
WORK_MIN = 25 * 60          # 25-minute focus periods
SHORT_BREAK_MIN = 5 * 60    # 5-minute short breathing periods
LONG_BREAK_MIN = 20 * 60    # 20-minute restorative breaks
```

