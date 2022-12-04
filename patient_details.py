from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image
from time import time

#Function for querying SQL for patient details
def patient_details_collect(username):
    #connect to mysql
    conn = mysql.connect(host="localhost",user="root",password="microsoft123")
        
    #create cursor        
    cursor = conn.cursor()
        
    #define input variable        
    sql_access_patient_details = ("SELECT * FROM patient_signup.patient_login WHERE patient_ic = '"+username+"'")
    cursor.execute(sql_access_patient_details)
    patient_details = cursor.fetchall()
    conn.commit()
    cursor.close()
    return patient_details

#To define 2 functions, pt view (read-only) and staff view (read and write)

def pt_details_pt_view(root_home,username):
    pt_details_pt_view = Toplevel(root_home)
    pt_details_pt_view.title("MCB: Your details")
    pt_details_pt_view.geometry("430x350")

    #running SQL query in function for patient details
    weird_list_tuple = patient_details_collect(username)
    print(weird_list_tuple)

    for patient_details_tuple in weird_list_tuple:
        print(patient_details_tuple)

    full_name=patient_details_tuple[3]
    blood_pressure=patient_details_tuple[4]
    spiro_oxy=patient_details_tuple[5]
    heart_rate=patient_details_tuple[6]
    temperature=patient_details_tuple[7]
    current_disease=patient_details_tuple[8]
    medical_history=patient_details_tuple[9]
    patient_weight=patient_details_tuple[10]
    patient_height=patient_details_tuple[11]
    patient_bmi=patient_details_tuple[12]
    patient_allergies=patient_details_tuple[13]
    patient_contact=patient_details_tuple[14]
    patient_emer_contact=patient_details_tuple[15]
    
    #creating labels
    welcome_text= Label(pt_details_pt_view, font=("Times",12), text="Your patient details, "+full_name)
    ic_label = Label(pt_details_pt_view,text="Identification Card Num.:")
    blood_pressure_label = Label(pt_details_pt_view,text="Blood Pressure:")
    spiro_oxy_label = Label(pt_details_pt_view,text="SpO2:")
    heart_rate_label = Label(pt_details_pt_view,text="Heart Rate:")
    temperature_label = Label(pt_details_pt_view,text="Body Temperature:")
    current_disease_label = Label(pt_details_pt_view,text="Current Diseases:")
    medical_history_label = Label(pt_details_pt_view,text="Medical History:")
    patient_weight_label = Label(pt_details_pt_view,text="Recent Weight:")
    patient_height_label = Label(pt_details_pt_view,text="Recent Height:")
    patient_bmi_label = Label(pt_details_pt_view,text="Recent BMI:")
    patient_allergies_label = Label(pt_details_pt_view,text="Known Allergies:")
    patient_contact_label = Label(pt_details_pt_view,text="Patient Contact Num.:")
    patient_emer_contact_label = Label(pt_details_pt_view,text="Patient Emergency Contact Num.:")

    #setting grid position for labels
    welcome_text.grid(row=0,column=0,columnspan=3)
    ic_label.grid(row=2,column=0)
    blood_pressure_label.grid(row=3,column=0)
    spiro_oxy_label.grid(row=4,column=0)
    heart_rate_label.grid(row=5,column=0)
    temperature_label.grid(row=6,column=0)
    current_disease_label.grid(row=7,column=0)
    medical_history_label.grid(row=8,column=0)
    patient_weight_label.grid(row=9,column=0)
    patient_height_label.grid(row=10,column=0)
    patient_bmi_label.grid(row=11,column=0)
    patient_allergies_label.grid(row=12,column=0)
    patient_contact_label.grid(row=13,column=0)
    patient_emer_contact_label.grid(row=14,column=0)

    #creating labels for output
    ic_output = Label(pt_details_pt_view,text=username)
    blood_pressure_output= Label(pt_details_pt_view,text=blood_pressure)
    spiro_oxy_output= Label(pt_details_pt_view,text=spiro_oxy)
    heart_rate_output= Label(pt_details_pt_view,text=heart_rate)
    temperature_output= Label(pt_details_pt_view,text=temperature)
    current_disease_output= Label(pt_details_pt_view,text=current_disease)
    medical_history_output= Label(pt_details_pt_view,text=medical_history)
    patient_weight_output= Label(pt_details_pt_view,text=patient_weight)
    patient_height_output= Label(pt_details_pt_view,text=patient_height)
    patient_bmi_output= Label(pt_details_pt_view,text=patient_bmi)
    patient_allergies_ouput= Label(pt_details_pt_view,text=patient_allergies)
    patient_contact_output= Label(pt_details_pt_view,text=patient_contact)
    patient_emer_contact_output= Label(pt_details_pt_view,text=patient_emer_contact)
    
    ic_output.grid(row=2,column=2)
    blood_pressure_output.grid(row=3,column=2)
    spiro_oxy_output.grid(row=4,column=2)
    heart_rate_output.grid(row=5,column=2)
    temperature_output.grid(row=6,column=2)
    current_disease_output.grid(row=7,column=2)
    medical_history_output.grid(row=8,column=2)
    patient_weight_output.grid(row=9,column=2)
    patient_height_output.grid(row=10,column=2)
    patient_bmi_output.grid(row=11,column=2)
    patient_allergies_ouput.grid(row=12,column=2)
    patient_contact_output.grid(row=13,column=2)
    patient_emer_contact_output.grid(row=14,column=2)

    def john():
        pt_details_pt_view.destroy()
        
    #Close button
    close_button_pt_details_pt_view = Button(pt_details_pt_view,text="Close",command=john,width=10).grid(row=15,column=1)
    
    
# def pt_details_staff_view(root_home,username):