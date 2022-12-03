# Import Tkinter

import tkinter as tk
from tkinter import *
from tkinter import ttk

# Adding Hello World to the Title and Main Screen
#root = Tk() makes the base window
root = Tk()
root.geometry("400x240")

#root.title("TITLE") prints the title on the root(base window)
root.title("MCB My Clinical Board")

#label is an empty field and  .pack() expands it to fill the root
label = Label(root, text="Hello World!")
label.grid()

#Tkinter event loop
root.mainloop()
