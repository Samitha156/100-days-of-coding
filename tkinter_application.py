from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="This is a label", font=("Arial", 24))
my_label.pack(side="left")

# my_label["text"] ="New text"
my_label.config(text="New text")


# Button


def button_clicked():
    print("I got clicked")
    NEW_TEXT = input.get()
    # my_label.config(text="I got clicked")
    my_label.config(text= NEW_TEXT)

def getting_text():
    print("enter")

input = Entry(width=10)
input.pack()
# print(input.get())

button = Button(text="click here", command=button_clicked)
button.pack()

#Entry






window.mainloop()


