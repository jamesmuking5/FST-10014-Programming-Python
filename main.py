from customtkinter import *
import tkinter
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image
import home_patient
import home_staff

#create base window and title and setting dimensions
root = CTk()
root.title("MCB Login")
root.geometry("550x300")

#Theme here
set_appearance_mode("Dark")
set_default_color_theme("blue")
root.attributes("-alpha",0.95)

#making an empty frame
logo_frame = CTkFrame(root,fg_color="transparent")
logo_frame.grid(rowspan=12,padx=40,pady=20)
#creating labels
main_label = CTkLabel(logo_frame,text="My Clinical Board Login",font=("Gadugi",18),wraplength=150,justify="center")
#frame position
main_label.grid()
#making picture
img = CTkImage(Image.open("./images/logo.png"),size=(150,150))
image_container= CTkLabel(logo_frame,image=img,text="")
image_container.grid()

#username password labels
username_label = CTkLabel(root,text="Username:",font=("Gadugi",15))
password_label = CTkLabel(root,text="Password:",font=("Gadugi",15))

#creating entries
username_entry = CTkEntry(root)
password_entry = CTkEntry(root, show="*")
 
#placing frames, labels and entries
username_label.grid(row=5,column=1,padx=10,rowspan=3)
password_label.grid(row=7,column=1,padx=10,rowspan=3)
username_entry.grid(row=5,column=2,rowspan=3)
password_entry.grid(row=7,column=2,rowspan=3)

#set focus to first entry
username_entry.focus_set()

#Radio button
staff_or_patient = StringVar(root,"1")
staff_login = CTkRadioButton(root, fg_color="#0129DA", text="Staff", variable=staff_or_patient, value="1")
patient_login = CTkRadioButton(root, fg_color="#0129DA",text="Patient", variable=staff_or_patient, value="2")

#Position radio button
staff_login.grid(row=2,column=2)
patient_login.grid(row=3,column=2)


#create function for login button
tries=3
def login():
    global username
    
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
            print("Should open home for staff")
            home_staff.root_home(root,username,img)
        elif staff_login.staff_login(username,password)==FALSE:
            tries-=1
            MessageBox.showerror("Wrong.","Wrong username and password. You have "+str(tries)+" tries left.")
        else:
            MessageBox.showerror("Error.","Please contact IT.")
               
    elif tries>0 and (staff_or_patient.get() == str(2)):
        #Import patient_login module
        import patient_login
        if patient_login.patient_login(username,password)==TRUE:
            print("Should open home for patients")
            home_patient.root_home(root,username,img)
        elif patient_login.patient_login(username,password)==FALSE:
            tries-=1
            MessageBox.showerror("Wrong.","Wrong username and password. You have "+str(tries)+" tries left.")
        else:
            MessageBox.showerror("Error.","Please contact IT.")
            
    elif tries<=0:
        MessageBox.showwarning("Try Limit.","You have reached the max amount of tries. Please try again later.")
    else:
        MessageBox.showerror("Error.","This should not happen.")
        
#creating a login button
login_button = CTkButton(root, text="Login",command=login,width=40,fg_color="red")
login_button.grid(row=13,column=2,padx=40,ipadx=40)
def click_signup():
    import signup
    signup.signup(root)

#creating a signup button
signup_button = CTkButton(root, text="Sign-up", command=click_signup,width=15,fg_color="green")
signup_button.grid(row=13,column=0)

#starting the main loop
root.mainloop()