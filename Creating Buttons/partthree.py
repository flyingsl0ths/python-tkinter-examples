from tkinter import *

# In tkinter everything is widget
# to create a window an instance of Tk()
# is needed along with that instances mainloop() method

root = Tk()


def say_hello():
    words = ["Navi says: ", "Hey", "Hello", "What\'s up", "Hey listen"]
    labels = [Label(root, text=words[i]).pack()
              for i in range(len(words))]


# Example of using the Button widget within and assigning it function
# object to be called whenever the button is clicked via command kwarg
my_button = Button(root, text="Click Me", padx=50,
                   command=say_hello, fg="#000000", bg="#ffffff")
my_button.pack()

root.mainloop()
