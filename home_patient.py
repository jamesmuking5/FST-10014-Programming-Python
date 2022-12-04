#Signup window
from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

def root_home(root,username):
    root_home = Toplevel(root)
    root_home.title ("Patient Details")
    root_home.geometry("1280x720")
        
    conn = mysql.connect(host="localhost",user="root",password="microsoft123")
            #create cursor
    cursor = conn.cursor()
            #define input variable
    cursor.execute("SELECT * FROM patient_signup.patient_login WHERE staff_ic = '"+ username +"'")
    #creating labels
    title_label = Label(root_signup,text="My Clinical Board Sign-up",width=20,padx=10,pady=10)
    name_label = Label(root_signup,text="Full Name:",pady=5)
    ic_label = Label(root_signup,text="Identification Card Number:",pady=5)
    password_label = Label(root_signup,text="New Password:",pady=5)
    password_label_check = Label(root_signup,text="New Password again:",pady=5)
    weight_label = Label(root_signup,text="Latest Weight(kg):",pady=5)
    height_label = Label(root_signup,text="Latest Height(cm):",pady=5)
    bmi_label = Label(root_signup,text="Latest BMI:",pady=5)
    allergy_label = Label(root_signup,text="Any allergies:",pady=5)
    contact_num_label = Label(root_signup,text="Contact Number:",pady=5)
    emer_contact_num_label = Label(root_signup,text="Emergency Contact Number:",pady=5)