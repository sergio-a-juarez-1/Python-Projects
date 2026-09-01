# 🍅 Tkinter Pomodoro Timer

A slick, desktop-based productivity application built in Python using the `tkinter` GUI framework. The app implements the classic **Pomodoro Technique**—cycling through focused work sessions punctuated by short and long breaks.

---

## 🚀 Features

*   **Classic Interval Flow**: Automatic cycling between 25-minute work rounds, 5-minute short breaks, and a 20-minute long break after 4 rounds.
*   **Visual Status Indicator**: Distinct layout color themes instantly signal your current state (Work 🟢, Short Break 💗, Long Break 🔴).
*   **Dynamic Milestones**: Automatically tracks your progress visually by displaying checkmarks (✓) for every completed work block.
*   **Zero Dependencies**: Relies solely on Python's built-in libraries.

---

## 🛠️ Installation

### 1. Prerequisites
Ensure you have **Python 3.x** installed. Tkinter typically comes pre-installed with standard Python distributions.

If you are on a Linux distribution and missing Tkinter, install it via your package manager:
```bash
sudo apt-get install python3-tk
```

### 2. File Architecture
Set up your local project directory as follows:
```text
pomodoro-app/
├── tomato.png      # The application logo image
└── main.py         # The core Python application script
```

---

## 💻 Usage

1. Save the source snippet code into a file named `main.py` inside your project directory.
2. Place your `tomato.png` icon asset in the same workspace directory (or update the file path reference on line 52 inside `main.py`).
3. Fire up the application terminal instance:

```bash
python main.py
```

### App Mechanics
*   **Start**: Kicks off the timer countdown mechanism.
*   **Reset**: Instantly resets the state back to zero, clears checks, and halts active loops.

---

## ⚙️ Configuration constants

You can easily adjust the cycle times directly near the top of `main.py`:

```python
# Values are calculated in seconds
WORK_MIN = 25 * 60          # 25-minute focus periods
SHORT_BREAK_MIN = 5 * 60    # 5-minute short breathing periods
LONG_BREAK_MIN = 20 * 60    # 20-minute restorative breaks
```
