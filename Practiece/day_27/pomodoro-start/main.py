from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Georgia"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# FONT_NAME = "Courier"

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Header_label.config(text="Pomodoro Timer")
    check_marks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """"""
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Header_label.config(text="Lonk Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Header_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        Header_label.config(text="Working Time", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """"""
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔︎"
        check_marks_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
#Creating a new window and configurations------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# setting tomato image to the window------------
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 137, text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


# Header Text-------------
Header_label = Label(text="Pomodoro Timer", font=("Georgia", 40), fg=GREEN, bg=YELLOW)
Header_label.config(pady=20)
Header_label.grid(column=1, row=0)

# Start Button------------
"""Configure start button. When start button is pressed it calls start_timer to start count down"""
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)
# Reset Button------------
end_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
end_button.grid(column=2, row=2)

# ✔︎ Text------------
check_marks_label = Label(font=("Georgia", 25), fg=GREEN, bg=YELLOW)
check_marks_label.grid(column=1, row=3)

window.mainloop()

