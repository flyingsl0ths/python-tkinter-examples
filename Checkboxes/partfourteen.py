from tkinter import *

root = Tk()
root.title("Window")
root.geometry("200x100")

theValue = IntVar()
choice = StringVar()

def get_status():
    global theValue
    status = theValue.get()

    print("on") if status == 0 else print("off")
    
def get_choice():
    global choice
    print(f"Choice: {choice.get()}")


cBox = Checkbutton(root, text="Checkbox#1",
                   variable=theValue, command=get_status)
cBox.pack()

# on/off values can be set via onvalue/offvalue
# this will be returned instead of the default 0/1
# by the variable wrapper's get() method this causes
# the button to be selected and greyed out (bug, caused due to
# the object taking in two parameters that represent on as on/off values)
# call deselect() before packing buttons initialized
# this way first
cBox2 = Checkbutton(root, text="Checkbox#2",
                   variable=choice, onvalue="On", offvalue="off", command=get_choice)
cBox2.deselect()
cBox2.pack()

root.mainloop()
