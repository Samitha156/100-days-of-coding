from tkinter import *
from tkinter import messagebox
import random
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# -------------- PASSWORD GENERATOR ------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(1, nr_letters + 1)]
    password_symbols = [random.choice(symbols) for sym in range(1, nr_symbols + 1)]
    password_numbers = [random.choice(symbols) for num in range(1, nr_numbers + 1)]

    password_list = password_numbers + password_symbols + password_letters

    # print(password_list)

    random.shuffle(password_list)
    # print(password_list)

    hard_password = "".join(password_list)
    # for character in password_list:
    #     hard_password += character
    # print(hard_password)
    password_entry.insert(0, hard_password)
    pyperclip.copy(hard_password)


# --------------- SAVE PASSWORD ----------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Oops", message="Please fill all entries")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {password} \n")

                password_entry.delete(0, END)
                website_entry.delete(0, END)
                website_entry.focus()


# --------------- UI SETUP ---------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="pad.png")
canvas.create_image(100, 80, image=padlock_image)
pass_text = canvas.create_text(100, 170, text="MyPass", fill=RED, font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=0)

# labels
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

email_text = Label(text="Email/Username:")
email_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "samitha156@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
