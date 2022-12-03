from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

root = Tk()
root.title("MCB Login")
root.geometry("250x400")

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

#creating menu


#creating entries
username_entry = Entry(root)
password_entry = Entry(root, show="*")
 
#placing frames, labels and entries
logo_frame.grid(row=0,column=0,rowspan=2,columnspan=7)
username_label.grid(row=5, column=1)
password_label.grid(row=6, column=1)
username_entry.grid(row=5, column=4)
password_entry.grid(row=6, column=4)

#frame position
main_label.grid(row=0, column=0)

#Radio button
staff_or_patient = StringVar(root,"1")
staff_login = Radiobutton(root, text="Staff", variable=staff_or_patient, value="1").grid(row=3,column=1)
patient_login = Radiobutton(root, text="Patient", variable=staff_or_patient, value="2").grid(row=3,column=4)



#create function for login button
tries=3
def login():    
    username = username_entry.get()
    password = password_entry.get()
    
    global tries
    
    if tries>0 and (username=="" or password==""):
        MessageBox.showinfo("Oops!","All fields are required.")
                    
    #check if user exist
    elif tries>0 and (staff_or_patient.get() == str(1)):
        #Import staff_login module
        import staff_login
        if staff_login.staff_login(username,password)==TRUE:            
            print("Should open home")
        elif staff_login.staff_login(username,password)==FALSE:
            tries-=1
            MessageBox.showerror("Wrong.","Wrong username and password. You have "+str(tries)+" tries left.")
        else:
            MessageBox.showerror("Error.","Please contact IT.")
               
    elif tries>0 and (staff_or_patient.get() == str(2)):
        #Import patient_login module
        import patient_login
        if patient_login.patient_login(username,password)==TRUE:
            print("Should open home")
        elif patient_login.patient_login(username,password)==FALSE:
            tries-=1
            MessageBox.showerror("Wrong.","Wrong username and password. You have "+str(tries)+" tries left.")
        else:
            MessageBox.showerror("Error.","Please contact IT.")
            
    elif tries<=0:
        MessageBox.showwarning("Try Limit.","You have reached the max amount of tries. Please try again later.")        
    
    else:
        MessageBox.showerror("Error.","This should not happen fam.")
        
#creating a login button
login_button = Button(root, text="Login", width=10, command=login)
login_button.grid(row=8, column=1, columnspan=2)

#shaping frames
empty_frame_1 = Frame(root,width=30).grid(row=7,column=0)
empty_frame_2 = Frame(root, height=30).grid(row=7, column=4)

def click_signup():
    import signup
    signup.signup(root)

#creating a signup button
signup_button = Button(root, text="Sign-up", width=10, command=click_signup)
signup_button.grid(row=8, column=4, columnspan=2)
 
#starting the main loop
root.mainloop()