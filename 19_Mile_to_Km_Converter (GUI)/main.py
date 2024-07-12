# imports
from formula import Formula
from tkinter import *

def button_clicked():
    """Convert to km when button clicked"""
    formula = Formula(int(user_input.get()))
    answer = round(formula.tokm,2)
    label_empty.config(text=answer)


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

# text 1st part in GUI
label_is_equal = Label(text="Miles is equal to")
# label.config(text="This is new text")
label_is_equal.grid(column=1, row=0)

# text 2nd part in GUI
label_empty = Label(text="__", font=("Arial", 18))
label_empty.grid(column=2, row=0)

# text in GUI
label_km = Label(text="Km")
label_km.grid(column=3, row=0)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=1)


window.mainloop()