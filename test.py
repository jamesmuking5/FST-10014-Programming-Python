from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image
from time import time

def root_home(root,username,img):
   root_home = Toplevel(root)
   root_home.title ("My Clinical Board - Home (Staff View)")
   root_home.geometry("550x400")
   
   #Make Sql Query for Full_name     
   conn = mysql.connect(host="localhost",user="root",password="microsoft123")
   #create cursor
   cursor = conn.cursor()
   #define input variable
   cursor.execute("SELECT * FROM patient_signup.patient_login WHERE patient_ic = '"+ username +"'")
   patient_login = cursor.fetchall()
   cursor.close()
   
   for x in patient_login:
      print(x)
      
   full_name = x[3]
    
   #creating labels
   title_label = Label(root_home,text="Welcome to My Clinical Board, Staff "+full_name+".",font=("Times", 15),pady=50)
   
   #Grid position
   title_label.grid(row=0,column=0,columnspan=3)
   
   #making picture
   image_frame = Frame(root_home,padx=10,pady=30)   
   image_frame.grid(row=1,column=0,columnspan=1,rowspan=2)   
   image_container_home = Label(image_frame,image=img)
   image_container_home.grid(row=0,column=0,columnspan=1,rowspan=2)
   
   #Define button command for patient details
   def start_patient_details():
      import patient_details
      patient_details.pt_details_pt_view(root_home,username)
   
   #making the 4 main buttons
   billing_button = Button(root_home, text="Billing Information", width="15", padx=10,pady=10)
   patient_details_button = Button(root_home, text="Patient's Details", command=start_patient_details, width="15", padx=10,pady=10)
   hotline_button = Button(root_home, text="Hotline", width="15", padx=10,pady=10)
   faq_button = Button(root_home, text="F.A.Q.", width="15", padx=10,pady=10)
   
   #Grid positioning for buttons
   billing_button.grid(row=1,column=1)
   patient_details_button.grid(row=1,column=2)
   hotline_button.grid(row=2,column=1)
   faq_button.grid(row=2,column=2)