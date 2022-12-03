# import libraries
import tkinter as tk
import mysql.connector as mysql
import signup_module

# create window
window = tk.Tk()
window.title("MySQL Login")
window.geometry("300x200")

# label
username_label = tk.Label(window, text="Username")
username_label.grid(row=0, column=0)

password_label = tk.Label(window, text="Password")
password_label.grid(row=1, column=0)

# entry
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

password_entry = tk.Entry(window, show='*')
password_entry.grid(row=1, column=1)

login(username_entry.get(), password_entry.get())

# button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=1)

window.mainloop()