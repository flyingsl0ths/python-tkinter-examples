from tkinter import *

user = "Sloths"

root = Tk()

blank0 = Label(root, text=f"Welcome, {user}")
blank0.pack()

username = Entry(root, width=50, borderwidth=1)
# In Tkinter input fields are known as an Entry() object
# they are placed within the window object as every other widget
username.insert(0, "Username")
username.pack()

blank = Label(root)
blank.pack()

password = Entry(root, width=50, borderwidth=1)
password.insert(0, "Password")
password.pack()

def check_if_empty(field):
    if field != "":
        return field
    else:
        return "empty"

def form():
    print([check_if_empty(i) for i in f"{username.get()} {password.get()}".split(" ")])

blank2 = Label(root)
blank2.pack()

my_button = Button(root, text="submit", command=form)
my_button.pack()

root.mainloop()
