from customtkinter import *
import tkinter
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

def signup(root):
    root_signup = CTkToplevel(root)
    root_signup.title("New User Signup")
    root_signup.geometry("390x650")
    
    #creating labels
    title_label = CTkLabel(root_signup,text="My Clinical Board Sign-up",font=("Calibri",18))
    name_label = CTkLabel(root_signup,text="Full Name:",font=("Gadugi",15))
    ic_label = CTkLabel(root_signup,text="Identification Card Number:",font=("Gadugi",15))
    password_label = CTkLabel(root_signup,text="New Password:",font=("Gadugi",15))
    password_label_check = CTkLabel(root_signup,text="New Password again:",font=("Gadugi",15))
    weight_label = CTkLabel(root_signup,text="Latest Weight(kg):",font=("Gadugi",15))
    height_label = CTkLabel(root_signup,text="Latest Height(cm):",font=("Gadugi",15))
    bmi_label = CTkLabel(root_signup,text="Latest BMI:",font=("Gadugi",15))
    allergy_label = CTkLabel(root_signup,text="Any allergies:",font=("Gadugi",15))
    contact_num_label = CTkLabel(root_signup,text="Contact Number:",font=("Gadugi",15))
    emer_contact_num_label = CTkLabel(root_signup,text="Emergency Contact Number:",font=("Gadugi",15))
    
    #setting grid position for labels
    title_label.grid(row=0,column=0,columnspan=2,padx=30,pady=80)
    name_label.grid(row=1,column=0,stick="w",padx=20)
    ic_label.grid(row=2,column=0,stick="w",padx=20)
    password_label.grid(row=3,column=0,stick="w",padx=20)
    password_label_check.grid(row=4,column=0,stick="w",padx=20)
    weight_label.grid(row=5,column=0,stick="w",padx=20)
    height_label.grid(row=6,column=0,stick="w",padx=20)
    bmi_label.grid(row=8,column=0,stick="w",padx=20)
    allergy_label.grid(row=9,column=0,stick="w",padx=20)
    contact_num_label.grid(row=10,column=0,stick="w",padx=20)
    emer_contact_num_label.grid(row=11,column=0,stick="w",padx=20)
    
    #creating inputs
    name_entry = CTkEntry(root_signup)
    ic_entry  = CTkEntry(root_signup)
    password_entry  = CTkEntry(root_signup, show="*")
    password_check_entry  = CTkEntry(root_signup, show="*")
    weight_entry = CTkEntry(root_signup)
    height_entry = CTkEntry(root_signup)
    bmi_entry  = CTkEntry(root_signup)
    allergy_entry  = CTkEntry(root_signup)
    contact_num_entry  = CTkEntry(root_signup)
    emer_contact_num_entry  = CTkEntry(root_signup)
    
    #setting grid position for inputs
    name_entry.grid(row=1,column=1)
    ic_entry.grid(row=2,column=1)
    password_entry.grid(row=3,column=1)
    password_check_entry.grid(row=4,column=1)
    weight_entry.grid(row=5,column=1)
    height_entry.grid(row=6,column=1)
    bmi_entry.grid(row=8,column=1)
    allergy_entry.grid(row=9,column=1)
    contact_num_entry.grid(row=10,column=1)
    emer_contact_num_entry.grid(row=11,column=1)
    
    #bmi calculator button function
    def calcBMI():
        weight = weight_entry.get()
        height = height_entry.get()
        if weight==str("") or height ==str(""):
            MessageBox.showerror("Oops.","Please input height and weight!")
        else:
            print("Miao")   
            BMI = round((float(weight)/((float(height)/100)**2)), 2)
            bmi_entry.delete(0, END)
            bmi_entry.insert(0, str(BMI))
        
    #bmi calculator button
    bmi_button = CTkButton(root_signup,text="Calculate BMI",command=calcBMI,fg_color="#5F5F5F")
    bmi_button.grid(row=7,column=1,pady=10)
    
    #reset button function
    def reset_signup():
        reset_sure = MessageBox.askyesno("Really?","Are you sure you want to reset everything?")
        if reset_sure==TRUE:
            name_entry.delete(0, END)
            ic_entry.delete(0, END)
            password_entry.delete(0, END)
            password_check_entry.delete(0, END)
            weight_entry.delete(0, END)
            height_entry.delete(0, END)
            bmi_entry.delete(0, END)
            allergy_entry.delete(0, END)
            contact_num_entry.delete(0, END)
            emer_contact_num_entry.delete(0, END)
        else:
            MessageBox.showinfo("Oops","Resetted all.")
            MessageBox.showinfo("Ehe","Just kidding.")
                
    #reset button
    reset_all = CTkButton(root_signup,text="Reset All",command=reset_signup,fg_color="#9C0606")
    reset_all.grid(row=12,column=1,pady=20)
    
 
    #confirmed submit
    def confirmed_submit_signup():
        
        #connect to mysql
        conn = mysql.connect(host="localhost",user="root",password="microsoft123")
        
        #create cursor        
        cursor = conn.cursor()
        
        #define input variable        
        sql_input_patient_data = ("INSERT INTO patient_signup.patient_login (patient_ic, patient_password, full_name, patient_weight, patient_height, bmi, allergies, patient_contact, patient_emergency) VALUES ('"+ic_entry.get()+"', '"+password_entry.get()+"', '"+name_entry.get()+"', '"+weight_entry.get()+"', '"+height_entry.get()+"', '"+bmi_entry.get()+"', '"+allergy_entry.get()+"', '"+bmi_entry.get()+"', '"+emer_contact_num_entry.get()+"');")
        #execute data
        cursor.execute(sql_input_patient_data)
        conn.commit()
        cursor.close()
        
    #submit button function
    def submit_signup():
        if password_entry.get() != password_check_entry.get():
            MessageBox.showerror("Warning!","Passwords do not match! Please try again.")
        elif (name_entry.get()=="" or ic_entry.get()=="" or password_entry.get()=="" or weight_entry.get()=="" or weight_entry.get()=="" or height_entry.get()=="" or allergy_entry.get()=="" or bmi_entry.get()=="" or bmi_entry.get()=="" or emer_contact_num_entry.get()==""):
            MessageBox.showerror("Empty fields!","All fields must be filled!") 
        else:
            confirmed_submit_signup()
            MessageBox.askquestion("Welcome.","Welcome to My Clinical Board. You can now sign in with your IC and password.")
            root_signup.destroy()      

    #submit button
    submit_button = CTkButton(root_signup,text="Submit",command=submit_signup,fg_color="#00C436").grid(row=13,column=1)
    
    #cancel button function
    def cancel():
        root_signup.destroy()
        
    #cancel button
    cancel_button = CTkButton(root_signup,text="Cancel",command=cancel,fg_color="#002CC4").grid(row=13,column=0,stick="w",padx=30)