from tkinter import *


root = Tk()

name = Entry(root, width=50, borderwidth=1)
name.insert(0, "Enter You Name")
name.pack()

blank = Label(root)
blank.pack()


def my_click():
    hello = "Hello " + name.get()
    my_label = Label(root, text=hello)
    my_label.pack()


my_button = Button(root, text="submit", command=my_click)
my_button.pack()

root.mainloop()
