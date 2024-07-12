# imports
from formula import Formula
from tkinter import *

def button_clicked():
    """Convert to km when button clicked"""
    formula = Formula(int(user_input.get()))
    answer = round(formula.tokm,2)
    label_2.config(text=answer)


# Window configuration
window = Tk()
window.title("Mile -> Km Converter")
window.minsize(width=500, height=300)
window.config(padx=150, pady=100)

# User input section
user_input = Entry(width=4)
#Add some text to begin with
user_input.insert(END, string="0")
#Gets text in entry
print(user_input.get())
user_input.grid(column=0, row=0)

# text in GUI
label_1 = Label(text="Miles is equal to")
# label.config(text="This is new text")
label_1.grid(column=1, row=0)

# Answer text
label_2 = Label(text="__", font=("Arial", 18))
label_2.grid(column=2, row=0)

# text in GUI
label_3 = Label(text="Km")
label_3.grid(column=3, row=0)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=1)


window.mainloop()