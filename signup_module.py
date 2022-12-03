import tkinter 
from tkinter import *
from tkinter import ttk

# Create root window
root = Tk()

# Create username and password variable
username = StringVar()
password = StringVar()

# Create login and signup function
def login():
    if username.get() == "admin" and password.get() == "admin":
        print("Login Successful!")
    else:
        print("Invalid username or password!")

def signup():
    root2 = TK()

# Create window size
root.geometry("200x100")

# Create window title
root.title("Login Form")

# Create label for username
username_label = Label(root, text="Username").grid(row=0, column=0)

# Create entry box for username
username = Entry(root, textvariable=username).grid(row=0, column=1)

# Create label for password
username_title = Label(root, text="Password").grid(row=1, column=0)

# Create entry box for password
password = Entry(root, textvariable=password).grid(row=1, column=1)

# Create radio button for login type
Radiobutton(root, text="Staff", value="staff").grid(row=2, column=0)
Radiobutton(root, text="Patient", value="patient").grid(row=2, column=1)

# Create button for login
login_button = Button(root, text="Login", command=login).grid(row=3, columnspan=2, sticky=W+E)

# Run main loop
root.mainloop()