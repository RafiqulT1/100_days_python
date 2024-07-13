from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Georgia"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# FONT_NAME = "Courier"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time

count = 5
while True:
    time.sleep(1)
    count -= 1
    print(count)

# ---------------------------- UI SETUP ------------------------------- #
#Creating a new window and configurations
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# setting tomato image to the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 137, text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Header Text
Header_lable = Label(text="Pomodoro Timer", font=("Georgia", 40), fg=GREEN, bg=YELLOW)
Header_lable.config(pady=20)
Header_lable.grid(column=1, row=0)

# Start Button
button = Button(text="Start", highlightbackground=YELLOW)
button.grid(column=0, row=2)
# Reset Button
button = Button(text="Reset", highlightbackground=YELLOW)
button.grid(column=2, row=2)

# ✔︎ Text
check_mark_lable = Label(text="✔︎", font=("Georgia", 25), fg=GREEN, bg=YELLOW)
check_mark_lable.grid(column=1, row=3)

window.mainloop()

