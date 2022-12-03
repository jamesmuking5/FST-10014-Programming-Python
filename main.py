from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

global root
root = Tk()
root.title("MCB Login")
root.geometry("250x350")

#making an empty frame
logo_frame = Frame(root)
#making picture
img = ImageTk.PhotoImage(Image.open("./logo.png"))
image_container= Label(logo_frame,image=img)
image_container.grid(row=1,column=0)


#creating labels
main_label = Label(logo_frame,text="My Clinical Board Login")
username_label = Label(root, text="Username:", pady=10)
password_label = Label(root, text="Password:")
 
#creating entries
username_entry = Entry(root)
password_entry = Entry(root, show="*")
 
#placing frames, labels and entries
logo_frame.grid(row=0,column=0,rowspan=2,columnspan=7)
username_label.grid(row=3, column=1)
password_label.grid(row=4, column=1)
username_entry.grid(row=3, column=4)
password_entry.grid(row=4, column=4)

#frame position
main_label.grid(row=0, column=0)

#create function for login button
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if(username=="" or password==""):
        MessageBox.showinfo("Oops!","All fields are required.")
    
    #check if user exist
    else:
        #Import staff_login module
        import staff_login
        staff_login.staff_login(username,password)
        
#creating a login button
login_button = Button(root, text="Login", width=10, command=login)
login_button.grid(row=7, column=1, columnspan=2)

#shaping frames
empty_frame_1 = Frame(root,width=100,height=30).grid(row=6,column=0,columnspan=7)
empty_frame_2 = Frame(root,width=30).grid(row=7,column=0)

def click_signup():
    import signup
    signup.signup(root)
    

#creating a signup button
signup_button = Button(root, text="Sign-up", width=10, command=click_signup)
signup_button.grid(row=7, column=4, columnspan=2)
 
#starting the main loop
root.mainloop()