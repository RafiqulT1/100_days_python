# Imports 
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Tkinter window and configuration
window = Tk()
window.title("Password Manager")
window.config(padx=45, pady=45)

# set image to Tkinter window
canvas = Canvas(width=200, height=190)
lock_image = PhotoImage(file="./logo.png")
canvas_image = canvas.create_image(100, 95, image=lock_image)
canvas.grid(column=1, row=0)

    #--------LABELS--------#
# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Email/Username label
Eml_username_lable = Label(text="Email/Username:")
Eml_username_lable.grid(column=0, row=2)
# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

    #--------ENTRIES--------#
# Website entry
Website_entry = Entry(width=35)
Website_entry.insert(END, string="enter website link") #Add some text to begin with
Website_entry.grid(column=1, row=1, columnspan=2)
# Email/Username entry
Eml_username_entry = Entry(width=35)
Eml_username_entry.insert(END, string="enter username or email") #Add some text to begin with
Eml_username_entry.grid(column=1, row=2, columnspan=2)
# Password entry
password_entry = Entry(width=21)
password_entry.insert(END, string="enter password") #Add some text to begin with
password_entry.grid(column=1, row=3)

    #--------BUTTONS--------#
# Generate Password button
generate_psw_button = Button(text="Generate Password", width=10)
generate_psw_button.grid(column=2, row=3)
# Add button
add_button = Button(text="Add", width=33)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()