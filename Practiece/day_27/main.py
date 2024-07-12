# import tkinter
from tkinter import *



def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Configure TKinker window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=50, pady=50)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
# my_label.place(x=180, y=0)#need this to place the component on the screen
my_label.grid(column=0, row=0)

#update text object
# my_label["text"] = "HEllO"
# my_label.config(text="new text")

#button
button = Button(text="click me!", command=button_clicked)
button.grid(column=1, row=1)
# button.config(padx=50, pady=50)
# button.pack()

#button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=3, row=2)



window.mainloop()
