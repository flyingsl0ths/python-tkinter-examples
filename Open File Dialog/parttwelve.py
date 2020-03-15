from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Window 1")

# filedialog returns a file object from
# an initial directory or a directory
# specified by tuples of file type and file extension pair
# in filetypes

my_img = 0


def open_img():
    global my_img
    # Example of using the pointer to an image file object
    # returned from filedialog an displaying it within root window
    root.filename = filedialog.askopenfile(
        initialdir="./res", title="Select A File", filetypes=(("png files", "*png"), ("jpg file", "*jpg"), ("all files", "*.*")))

    my_img = ImageTk.PhotoImage(Image.open(root.filename.name))
    my_lbl = Label(root, image=my_img)
    my_lbl.pack()


my_button = Button(root, text="open image", command=open_img)
my_button.pack()

mainloop()
