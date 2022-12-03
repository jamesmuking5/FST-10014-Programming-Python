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
    title_label = Label(root_signup,text="My Clinical Board Sign-up",width=20,padx=10,pady=10)
    name_label = Label(root_signup,text="First Name:",pady=5)
    ic_label = Label(root_signup,text="Identification Card Number:",pady=5)
    password_label = Label(root_signup,text="New Password:",pady=5)
    password_label_check = Label(root_signup,text="New Password again:",pady=5)
    weight_label = Label(root_signup,text="Latest Weight(kg):",pady=5)
    height_label = Label(root_signup,text="Latest Height(cm):",pady=5)
    bmi_label = Label(root_signup,text="Latest BMI:",pady=5)
    allergy_label = Label(root_signup,text="Any allergies:",pady=5)
    contact_num_label = Label(root_signup,text="Contact Number:",pady=5)
    emer_contact_num_label = Label(root_signup,text="Emergency Contact Number:",pady=5)
    
    #setting grid position for labels
    title_label.grid(row=0,column=0,columnspan=3)
    name_label.grid(row=1,column=0)
    ic_label.grid(row=2, column=0)
    password_label.grid(row=3,column=0)
    password_label_check.grid(row=4,column=0)
    weight_label.grid(row=5,column=0)
    height_label.grid(row=6,column=0)
    bmi_label.grid(row=8,column=0)
    allergy_label.grid(row=9,column=0)
    contact_num_label.grid(row=10,column=0)
    emer_contact_num_label.grid(row=11,column=0)
    
    #creating inputs
    name_entry = Entry(root_signup)
    ic_entry  = Entry(root_signup)
    password_entry  = Entry(root_signup)
    password_check_entry  = Entry(root_signup)
    weight_entry = Entry(root_signup)
    height_entry = Entry(root_signup)
    bmi_entry  = Entry(root_signup)
    allergy_entry  = Entry(root_signup)
    contact_num_entry  = Entry(root_signup)
    emer_contact_num_entry  = Entry(root_signup)
    
    #setting grid position for inputs
    name_entry.grid(row=1,column=3)
    ic_entry.grid(row=2,column=3)
    password_entry.grid(row=3,column=3)
    password_check_entry.grid(row=4,column=3)
    weight_entry.grid(row=5,column=3)
    height_entry.grid(row=6,column=3)
    bmi_entry.grid(row=8,column=3)
    allergy_entry.grid(row=9,column=3)
    contact_num_entry.grid(row=10,column=3)
    emer_contact_num_entry.grid(row=11,column=3)
    
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
    bmi_button = Button(root_signup,text="Calculate BMI",width=10,command=calcBMI).grid(row=7,column=3)
    
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
    reset_all = Button(root_signup,text="Reset All",width=10,command=reset_signup).grid(row=12,column=1)
    
    #submit button function
    def submit_signup():
        #connect to mysql
        conn = mysql.connect(host="localhost",user="root",password="microsoft123")
        #create cursor
        cursor = conn.cursor()
        #define input variable
        sql_input_patient_data = ("INSERT INTO patient_signup.patient_login (patient_ic, patient_password, full_name, patient_weight, patient_height, bmi, allergies, patient_contact, patient_emergency) VALUES ('"+ic_entry.get()+"', '"+password_entry.get()+"', '"+name_entry.get()+"', '"+weight_entry.get()+"', '"+height_entry.get()+"', '"+bmi_entry.get()+"', '"+allergy_entry.get()+"', '"+contact_num_entry.get()+"', '"+emer_contact_num_entry.get()+"');")
        #execute data
        cursor.execute(sql_input_patient_data)
    
    #submit button
    submit_button = Button(root_signup,text="Submit",width=10,command=submit_signup).grid(row=12,column=3)
    
    #cancel button function
    def cancel():
        root_signup.destroy()
        
    #cancel button
    cancel_button = Button(root_signup,text="Cancel",width=10,command=cancel).grid(row=12,column=0)
    
    #making an empty frame
    # signup_frame = Frame(root_signup).grid(row=0,column=0)
    # #making picture
    # img = ImageTk.PhotoImage(Image.open("./logo.png"))
    # image_container= Label(signup_frame,image=img)
    # image_container.grid(row=1,column=0)