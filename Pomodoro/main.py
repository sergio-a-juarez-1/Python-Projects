from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
BG = "#050E3C"
PINK = "#FF3838"
RED = "#DC0000"
GREEN = "#9bdeac"
BLUE = "#002455"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=BG)
    reps = 0
    check.config(text='')



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(fg=RED, text="Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(fg=PINK, text="Break")
    elif reps %2 != 0:
        count_down(WORK_MIN)
        timer_label.config(fg=GREEN, text="Work")
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("🍅 Pomodoro 🍅")
window.config(padx=100, pady=50, bg=BG)



canvas = Canvas(width=200,height=224, bg=BG, highlightthickness=0)
tomato_img = PhotoImage(file="/root/Downloads/pomodoro/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME,35, 'bold'))
canvas.grid(row=1,column=1)


## Timer
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=BG, highlightthickness=0)
timer_label.grid(row=0,column=1)

## Buttons
start = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, fg=BLUE, bg=GREEN, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, fg=BLUE, bg=RED, command=reset_timer)
reset.grid(row=2, column=2)

# Check mark
check = Label(text="", font=(FONT_NAME, 25, "bold"), bg=BG, fg=GREEN)
check.grid(row=3, column=1)

window.mainloop()