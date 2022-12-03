from tkinter import *
 
root = Tk()
root.title("Login")
 
#creating labels
username_label = Label(root, text="Username:")
password_label = Label(root, text="Password:")
 
#creating entries
username_entry = Entry(root)
password_entry = Entry(root, show="*")
 
#placing labels and entries
username_label.grid(row=0, column=0)
password_label.grid(row=1, column=0)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
 
#creating a login button
login_button = Button(root, text="Login", width=10)
login_button.grid(row=2, column=0, columnspan=2)
 
#starting the main loop
root.mainloop()