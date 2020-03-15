import os
from tkinter import *
from PIL import ImageTk, Image

i = 0
img_path = "./res"
os.chdir(img_path)
img_dir = os.listdir()
imgs = []
img_names = []

root = Tk()
root.title("Gallery")

for img in img_dir:
    file_name, extn = os.path.splitext(img)
    if(extn == ".png" or extn == ".jpg"):
        curr_img = ImageTk.PhotoImage(Image.open(img))
        imgs.append(curr_img)
        img_names.append(img)


my_label = Label(image=imgs[0])
my_label.grid(row=0, column=0, columnspan=3)


status = Label(
    root, text=f"Image: {i+1} of {len(imgs)}\t\t\t\tName: {img_names[0]}", bd=1, relief=SUNKEN, anchor=W, pady=2)


def forward():
    global i
    if i < len(imgs)-1:
        global my_label
        global status
        i = i + 1
        my_label.grid_forget()
        my_label["image"] = imgs[i]
        my_label.grid(row=0, column=0, columnspan=3)
        status["text"] = f"Image: {i+1} of {len(imgs)}\t\t\t\tName: {img_names[i]}"


def back():
    global i
    if i > 0:
        global my_label
        i = i - 1
        my_label.grid_forget()
        my_label["image"] = imgs[i]
        my_label.grid(row=0, column=0, columnspan=3)
        status["text"] = f"Image: {i+1} of {len(imgs)}\t\t\t\tName: {img_names[i]}"


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
