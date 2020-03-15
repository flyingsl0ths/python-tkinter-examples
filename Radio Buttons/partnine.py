from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("window")

my_frame = LabelFrame(root, padx=100, pady=100)


TOPPINGS = ["Pepperoni", "Cheese", "Mushroom", "Onion"]

# Tkinter variables can be used to keep track of
# the value of a radio button whose is
# assigned this variable wrapper class when accessed
# Radiobutton(my_frame, text=topping, variable=pizza, value=topping)
pizza = StringVar()

my_label = Label(my_frame, text="Type of pizza?")
my_label.pack()

def change(topping):
    global my_label
    my_label["text"] = f"{topping} pizza"
    
def place_order(topping):
    global my_label
    my_label["text"] = f"Order placed for {topping} pizza"

for topping in TOPPINGS:
    Radiobutton(my_frame, text=topping, variable=pizza, value=topping, command=lambda: change(pizza.get())).pack()
    
order_Button = Button(my_frame, text="place order", command=lambda: place_order(pizza.get())).pack()
my_frame.pack(padx=10, pady=10)

root.mainloop()