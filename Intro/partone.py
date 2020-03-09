from tkinter import *

# In tkinter everything is widget
# to create a window an instance of TK()
# is needed along with that instances mainloop() method

root = Tk()

# Adding widgets to a TK instance()
my_label = Label(root, text="Hello!")
# Packs the widget in the first available location
my_label.pack()

root.mainloop()
