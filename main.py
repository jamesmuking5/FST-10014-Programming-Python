# import libraries
import tkinter as tk
import mysql.connector as mysql

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

# function
def login():
    username = username_entry.get()
    password = password_entry.get()

    # connect to mysql
    conn = mysql.connect(
        host="localhost",
        user=username,
        passwd=password
    )

    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()
    print("Database version : %s " % data)

# button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=1)

window.mainloop()