# import Tkinter
from tkinter import *

inKm = 10

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
label = Label(text="Miles is equal to")
# label.config(text="This is new text")
label.grid(column=1, row=0)

# Answer text
label = Label(text="ANSWER", font=("Arial", 18))
label.config(text=inKm)
label.grid(column=2, row=0)

# text in GUI
label = Label(text="Km")
label.grid(column=3, row=0)

# Button
button = Button(text="Calculate")
button.grid(column=1, row=1)



window.mainloop()