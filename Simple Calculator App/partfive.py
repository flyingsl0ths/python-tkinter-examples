from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Label(root, text="", bg="white",  width=40, borderwidth=5)

e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def insert_text(text):
    e["text"] = text

def button_clear():
    insert_text("")

def button_click(symbol):
    current = e["text"]
    button_clear()
    insert_text(current + symbol)
       
def button_eval():
    current = e["text"]
    button_clear()
    if(current != ""): insert_text(str(eval(current)))
    
    
button_1 = Button(root, text="1", padx=40, pady=30, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=40, pady=30, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=40, pady=30, command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=40, pady=30, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=40, pady=30, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=40, pady=30, command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=40, pady=30, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=40, pady=30, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=40, pady=30, command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=40, pady=30, command=lambda: button_click("0"))
button_add = Button(root, text="+", padx=39, pady=30, command=lambda: button_click("+"))
button_sub = Button(root, text="-", padx=39, pady=30, command=lambda: button_click("-"))
button_mult = Button(root, text="*", padx=39, pady=30, command=lambda: button_click("*"))
button_div = Button(root, text="/", padx=39, pady=30, command=lambda: button_click("/"))
button_eq = Button(root, text="=", padx=39, pady=30, command=button_eval)
button_clr = Button(root, text="c", padx=39, pady=30, command=button_clear)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mult.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clr.grid(row=4, column=1)
button_eq.grid(row=4, column=2)
button_div.grid(row=4, column=3)


root.mainloop()
