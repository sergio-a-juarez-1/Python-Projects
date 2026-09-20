import tkinter as tk
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
BG = "#050E3C"
PINK = "#FF3838"
RED = "#DC0000"
GREEN = "#9bdeac"
BLUE = "#002455"
TEXT_COLOR = "#FFFFFF" # Added for readable timer numbers over a dark canvas
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None
is_running = False # Tracks if the timer loop is active

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer, is_running
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check.config(text='')
    reps = 0
    is_running = False

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, is_running
    # Prevent duplicate timer loops if start button is spam-clicked
    if is_running:
        return
        
    is_running = True
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(fg=RED, text="Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(fg=PINK, text="Break")
    else:
        count_down(WORK_MIN)
        timer_label.config(fg=GREEN, text="Work")
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer, is_running
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    # Clean zero-padding formatting
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        is_running = False # Let the next session safely initiate a loop
        start_timer()
        mark = "✓" * math.floor(reps / 2)
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("🍅 Pomodoro 🍅")
window.config(padx=100, pady=50, bg=BG)

# Target the asset dynamically relative to where main.py runs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "tomato.png")

canvas = tk.Canvas(width=200, height=224, bg=BG, highlightthickness=0)
try:
    tomato_img = tk.PhotoImage(file=IMAGE_PATH)
    canvas.create_image(100, 112, image=tomato_img)
except tk.TclError:
    # Fallback to a clean blank shape layout if the image file is missing
    canvas.create_oval(20, 30, 180, 190, fill=PINK, outline="")

# Added fill=TEXT_COLOR to ensure numbers show up beautifully over the image
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, 'bold'), fill=TEXT_COLOR)
canvas.grid(row=1, column=1)

## Timer Label
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=BG)
timer_label.grid(row=0, column=1)

## Buttons
start = tk.Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, fg=BLUE, bg=GREEN, command=start_timer)
start.grid(row=2, column=0)

reset = tk.Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, fg=BLUE, bg=RED, command=reset_timer)
reset.grid(row=2, column=2)

# Check marks
check = tk.Label(text="", font=(FONT_NAME, 25, "bold"), bg=BG, fg=GREEN)
check.grid(row=3, column=1)

window.mainloop()

