from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=20)

#Labels
label = Label()
label.config(text="is equal to")
label.grid(column=0, row=1)


#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="")
#Gets text in entry
user_input = entry.get()
# user_num = int(user_input)
# print(entry.get())
entry.grid(column=1, row=0)

def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")

#calls action() when pressed
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


#Labels
km_result = Label(text="0")
km_result.grid(column=1, row=1)

#Labels
label = Label()
label.config(text="Miles")
label.grid(column=2, row=0)

#Labels
label = Label()
label.config(text="Km")
label.grid(column=2, row=1)




window.mainloop()