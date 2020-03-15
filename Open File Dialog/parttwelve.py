from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Window 1")

# filedialog returns a file object from
# an initial directory or a directory
# specified by tuples of file type and file extension pair
# in filetypes
root.filename = filedialog.askopenfile(
    initialdir="./res", title="Select A File", filetypes=(("png files", "*png"), ("jpg file", "*jpg"), ("all files", "*.*")))

# Example of using the image file object returned from filedialog
# an displaying it within root window
my_img = ImageTk.PhotoImage(Image.open(root.filename.name))
my_lbl = Label(root, image=my_img)
my_lbl.pack()

mainloop()
