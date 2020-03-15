from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Window 1")

my_img = 0

def new_wndow():
    global my_img
    top = Toplevel()
    top.title("Window 2")
    my_img = ImageTk.PhotoImage(Image.open("./res/pika.png"))
    my_lbl = Label(top, image=my_img)
    my_lbl.pack()
    my_btn = Button(top, text="close window", command=top.destroy)
    my_btn.pack()
    
butn = Button(root, text="new window", command=new_wndow)
butn.pack()

mainloop()
