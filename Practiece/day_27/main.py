# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label.pack() #need this to place the component on the screen

#update text object
# my_label["text"] = "HEllO"
my_label.config(text="new text")


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#button
button = Button(text="click me!", command=button_clicked)
button.pack()


#Entry

input = Entry(width=10)
input.pack()
print(input.get())



window.mainloop()
