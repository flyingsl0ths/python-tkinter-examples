from tkinter import *

# In tkinter everything is widget
# to create a window an instance of Tk()
# is needed along with that instances mainloop() method

root = Tk()

# Adding widgets to a TK instance()
# my_label1 = Label(root, text="Hello World!")
# my_label2 = Label(root, text="Hello World!")

words = ["Navi says: ", "Hey", "Hello", "What\'s up", "Hey listen"]
labels = [Label(root, text=words[i]).grid(row=i, column=i+1)
          for i in range(len(words))]

# labels = [Label(root, text=words[i]).pack()
#           for i in range(len(words))]

# Gridlayout System works by placing widgets on columns & rows
# if the number of columns specified is > number of widgets within
# Tk, it is ignored and widget is placed within relative location
# my_label1.grid(row=0, column=0)
# my_label2.grid(row=1, column=5)

root.mainloop()
