from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Window 1")

labl = Label(root, text="Response is: ")
labl.pack()

def poppedUp():
    global labl
    response = messagebox.askokcancel("info", "hello")
    # showinfo: ok, showwarning: ok, showerror: ok,
    # askquestion: yes/no, asokcancel: true/false,
    # askyesorno: true/fasle 
    labl["text"] = f"Response is: {response}"
    

button1 = Button(root, text="Popup", command=poppedUp)
button1.pack()

mainloop()
