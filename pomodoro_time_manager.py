from tkinter import *
import time
import math

# -------------------------CONSTANTS------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ------------------------ TIMER RESET ---------------------#

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_time, text="00:00")
    timer_text.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ------------------------- TIMER MECHANISM ----------------#
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        timer_text.config(text=f"Work {WORK_MIN} minutes", fg=YELLOW)
    elif reps == 8:
        count_down(long_break_sec)
        timer_text.config(text=f"Take {LONG_BREAK_MIN} minutes break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_text.config(text=f"Take {SHORT_BREAK_MIN} minutes break", fg=PINK)

# -------------------------- COUNTDOWN MECHANISM -----------#
def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
        canvas.itemconfig(timer_time, text=f"{min}:{sec}")

    canvas.itemconfig(timer_time, text=f"{min}:{sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_mark.config(text=mark)

# -------------------------- UI SETUP ----------------------#

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=GREEN)


canvas = Canvas(width=300, height=300, bg=GREEN, highlightthickness=0)
clock_img = PhotoImage(file="ccc.png")
canvas.create_image(150, 170, image=clock_img)
timer_time = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 45))
canvas.grid(column=1, row=1)

timer_text = Label(text="Timer", fg=YELLOW, bg= GREEN, font=(FONT_NAME, 35, "bold"))
timer_text.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=YELLOW, bg= GREEN)
check_mark.grid(column=1, row=3)


window.mainloop()