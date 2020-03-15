from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("window")

# Widgets within a LabelFrame can use
# a different layoutmanager than the frame itself
my_frame = LabelFrame(root, padx=50, pady=50)
my_frame.pack(padx=10, pady=10)

button1 = Button(my_frame, text="somethin")
button1.grid(row=0, column=0)

button2 = Button(my_frame, text="somethin")
button2.grid(row=1, column=1)

root.mainloop()