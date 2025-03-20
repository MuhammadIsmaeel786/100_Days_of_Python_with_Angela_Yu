from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


entry = Entry(width=10)
entry.grid(column=1, row=0)
entry.focus()
entry.insert(END, string="0")
text = Label(text="Miles", font=("Helvetica", 10, "normal"))
text.grid(column=2, row=0)
km = Label(text="0", font=("Times", 10))
km.grid(column=1, row=1)
text = Label(text="Km", font=("Times", 10, "normal"))
text.grid(column=2, row=1)
is_equal = Label(text="is equal to", font=("Times", 10))
is_equal.grid(column=0, row=1)

def calculate():
    entry_value = float(entry.get())
    km.config(text=entry_value * 1.609)
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)




window.config(padx=100, pady=100)
window.mainloop()