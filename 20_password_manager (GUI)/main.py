# Imports 
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # call get_info function to get website, email & password from entry
    website, email_or_username, password = get_info()

    if not website or not password or not email_or_username:
        messagebox.showinfo(title="Warning", message="Please fill all the empty fields")
    else: 
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_or_username} "
                            f"\nPassword:{password} \nIs it ok to save?")
        
        if is_ok:
            with open("saved_data.txt", mode="a") as password_file:
                password_file.write(f"✤ {website} | {email_or_username} | {password}\n")

            # call clear_info function to empty entries
        clear_info()

def get_info():
    website = Website_entry.get()
    email_or_username = Eml_username_entry.get()
    password = password_entry.get()

    return website, email_or_username, password

def clear_info():
    Website_entry.delete(0, "end")
    Eml_username_entry.delete(0, "end")
    password_entry.delete(0, "end")
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
# Website_entry.insert(END, string="enter website link") #Add some text to begin with
Website_entry.focus() #auto set cursor to website entry box
Website_entry.grid(column=1, row=1, columnspan=2)
# Email/Username entry
Eml_username_entry = Entry(width=35)
# Eml_username_entry.insert(END, string="enter username or email") #Add some text to begin with
Eml_username_entry.grid(column=1, row=2, columnspan=2)
# Password entry
password_entry = Entry(width=20)
# password_entry.insert(END, string="enter password") #Add some text to begin with
password_entry.grid(column=1, row=3)

    #--------BUTTONS--------#
# Generate Password button
generate_psw_button = Button(text="Generate Password", width=11)
generate_psw_button.grid(column=2, row=3)
# Add button
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()