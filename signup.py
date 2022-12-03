#Signup window
from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

def signup(root):
    root_signup = Toplevel(root)
    root_signup.title("New User Signup")
    root_signup.geometry("1280x720")
    
    #creating labels
    name_label = Label(root_signup,text="First Name:",pady=5).grid(row=0,column=0)
    ic_label = Label(root_signup,text="Identification Card Number:",pady=5).grid(row=1, column=0)
    password_label = Label(root_signup,text="New Password:",pady=5).grid(row=2,column=0)
    password_label_check = Label(root_signup,text="New Password again:",pady=5).grid(row=3,column=0)
    weight_label = Label(root_signup,text="Latest Weight:",pady=5).grid(row=4,column=0)
    height_label = Label(root_signup,text="Latest Height:",pady=5).grid(row=5,column=0)
    bmi_label = Label(root_signup,text="Latest BMI:",pady=5).grid(row=7,column=0)
    allergy_label = Label(root_signup,text="Any allergies:",pady=5).grid(row=8,column=0)
    contact_num_label = Label(root_signup,text="Contact Number:",pady=5).grid(row=9,column=0)
    emer_contact_num_label = Label(root_signup,text="Emergency Contact Number:",pady=5).grid(row=10,column=0)
    
    #creating inputs
    name_entry = Entry(root_signup).grid(row=0,column=1)
    ic_entry  = Entry(root_signup).grid(row=1,column=1)
    password_entry  = Entry(root_signup).grid(row=2,column=1)
    password_check_entry  = Entry(root_signup).grid(row=3,column=1)
    weight_entry  = Entry(root_signup).grid(row=4,column=1)
    height_entry  = Entry(root_signup).grid(row=5,column=1)
    bmi_entry  = Entry(root_signup).grid(row=7,column=1)
    allergy_entry  = Entry(root_signup).grid(row=8,column=1)
    contact_num_entry  = Entry(root_signup).grid(row=9,column=1)
    emer_contact_num_entry  = Entry(root_signup).grid(row=10,column=1)
    
    #bmi calculator
    def calcBMI():
        weight = int(weight_entry.get())
        height = int(height_entry.get())
        BMI = weight//(height*2)
        bmi_entry.insert(BMI)
        
    #bmi button
    bmi_button = Button(root_signup,text="Calculate BMI",width=10,command=calcBMI).grid(row=6,column=0,columnspan=2)
    
   
        
    
    #making an empty frame
    # signup_frame = Frame(root_signup).grid(row=0,column=0)
    # #making picture
    # img = ImageTk.PhotoImage(Image.open("./logo.png"))
    # image_container= Label(signup_frame,image=img)
    # image_container.grid(row=1,column=0)