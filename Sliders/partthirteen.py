from tkinter import *

root = Tk()
root.title("Window")
root.geometry("500x500")


def update_window_size(x, y):
    if x and y:
        root.geometry(f"{x}x{y}")


vertical_scrll = Scale(root, from_=0, to=1000)

horizontal_scrll = Scale(root, from_=0, to=1000, orient=HORIZONTAL)

my_btn = Button(root, text="Change Window Size", command=lambda: update_window_size(
    horizontal_scrll.get(), vertical_scrll.get()))


vertical_scrll.pack()
horizontal_scrll.pack()
my_btn.pack()

root.mainloop()
