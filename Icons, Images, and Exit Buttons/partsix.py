from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Art")

# Example of loading an image using Pillow into Tkinter
my_img = ImageTk.PhotoImage(Image.open(r'Icons, Images, and Exit Buttons/art.jpg'))
my_label = Label(root, image=my_img)
my_label.pack()

# Example of binding quit() to button
button_quit = Button(root, text="exit", command=root.quit)
button_quit.pack()


root.mainloop()
