#Signup window
from customtkinter import *
import tkinter
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

def root_home(root,username,img):
   root_home = CTkToplevel(root)
   root_home.title ("My Clinical Board - Home")
   root_home.geometry("620x400")
   
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
      patient_details.pt_details_pt_view(root_home,username)
   def billing():
      MessageBox.showerror("Not lazy to do.","Work in Progress, will be available at next update.")
   def hotline_click():
      import messenger
      MessageBox.showinfo("Hotline.",messenger.Hotline())
   def faq_click():
      import messenger
      MessageBox.showinfo("FAQ",messenger.faq())
   #making the 4 main buttons
   billing_button = CTkButton(root_home, text="Billing Information", command=billing,fg_color="transparent")
   patient_details_button = CTkButton(root_home, text="Your Details", command=start_patient_details,fg_color="transparent")
   hotline_button = CTkButton(root_home, text="Hotline",fg_color="transparent",command=hotline_click)
   faq_button = CTkButton(root_home, text="F.A.Q.",fg_color="transparent",command=faq_click)
   
   #Grid positioning for buttons
   billing_button.grid(row=1,column=1,ipadx=40,ipady=40)
   patient_details_button.grid(row=1,column=2,ipadx=40,ipady=40)
   hotline_button.grid(row=2,column=1,ipadx=40,ipady=40)
   faq_button.grid(row=2,column=2,ipadx=40,ipady=40)