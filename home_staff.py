from customtkinter import *
import tkinter
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

#Create Home Page for staff
def root_home(root,username,img):
   root_home = CTkToplevel(root)
   root_home.title ("My Clinical Board - Home")
   root_home.geometry("620x400")
   
   #Make SQL Query for full_name     
   conn = mysql.connect(host="localhost",user="root",password="microsoft123")
   
   #create cursor
   cursor = conn.cursor()
   
   #define input variable
   cursor.execute("SELECT * FROM patient_signup.staff_login WHERE staff_ic = '"+ username +"'")
   staff_login = cursor.fetchall()
   cursor.close()
   
   #For single loop to retrieve tuple from list
   for x in staff_login:
      print("Retrieve",x,"from staff_login")
      
   full_name = x[4]
    
   #creating Welcome
   title_label = CTkLabel(root_home,text="Welcome to My Clinical Board, "+full_name+".",font=("Gadugi", 18))
   
   #Title Label Grid position
   title_label.grid(row=0,column=0,columnspan=3,pady=80)
   
   #making picture
   image_frame = CTkFrame(root_home,fg_color="transparent")   
   image_frame.grid(row=1,column=0,rowspan="3",padx=30)   
   image_container_home = CTkLabel(image_frame,image=img,text="")
   image_container_home.grid(row=0,column=0)
   
   #Define button command for patient details
   def start_patient_details():
      import patient_details
      patient_details.pt_details_staff_view(root_home,username)
   def billing():
      MessageBox.showerror("Not lazy to do.","Work in Progress, will be available at next update.")
   #making the 4 main buttons
   billing_button = CTkButton(root_home, text="Billing Information", command=billing,fg_color="transparent")
   patient_details_button = CTkButton(root_home, text="Your Details", command=start_patient_details,fg_color="transparent")
   hotline_button = CTkButton(root_home, text="Hotline",fg_color="transparent")
   faq_button = CTkButton(root_home, text="F.A.Q.",fg_color="transparent")
   
   #Grid positioning for buttons
   billing_button.grid(row=1,column=1,ipadx=40,ipady=40)
   patient_details_button.grid(row=1,column=2,ipadx=40,ipady=40)
   hotline_button.grid(row=2,column=1,ipadx=40,ipady=40)
   faq_button.grid(row=2,column=2,ipadx=40,ipady=40)