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
   cursor.execute("SELECT * FROM patient_signup.patient_login WHERE patient_ic = '"+ username +"'")
   patient_login = cursor.fetchall()
    
   #creating labels
   title_label = Label(root_home,text="My Clinical Board Sign-up",width=20, anchor="e", padx=10, pady = 10) 
   label = Label(root_home,text="Full Name:", anchor="e", pady=5)
   ic_label = Label(root_home,text="Identification Card Number:", anchor="e",pady=5)
 

   #setting grid position for labels
   title_label.grid(row=0,column=0,columnspan=3)
   password_label.grid(row=3,column=0)
   password_label_check.grid(row=4,column=0)
   weight_label.grid(row=5,column=0)
   height_label.grid(row=6,column=0)
   bmi_label.grid(row=8,column=0)
   allergy_label.grid(row=9,column=0)
   contact_num_label.grid(row=10,column=0)
   emer_contact_num_label.grid(row=11,column=0)


    