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
    pt_details_pt_view = Tk(root_home)
    pt_details_pt_view.title("MCB: Your details")
    pt_details_pt_view.geometry("1280x720")

    #running SQL query in function for patient details
    weird_list_tuple = patient_details_collect(username)
    print(weird_list_tuple)A

    for patient_details_tuple in weird_list_tuple:
        print(patient_details_tuple)

    #creating labels
    welcome_text= Label(pt_details_pt_view, text="Welcome,")
    name_label = Label(pt_details_pt_view,text=patient_details_tuple[3])
    ic_label = Label(pt_details_pt_view,text=patient_details_tuple[1])
    blood_pressure_label = Label(pt_details_pt_view,text=patient_details_tuple4[])
    spiro_oxy_label = Label(pt_details_pt_view,text=patient_details_tuple[5])
    heart_rate_label = Label(pt_details_pt_view,text=patient_details_tuple[6])
    temperature_label = Label(pt_details_pt_view,text=patient_details_tuple[7])
    current_disease_label = Label(pt_details_pt_view,text=patient_details_tuple[8])
    medical_history_label = Label(pt_details_pt_view,text=patient_details_tuple[9])
    patient_weight_label = Label(pt_details_pt_view,text=patient_details_tuple[10])
    patient_height_label = Label(pt_details_pt_view,text=patient_details_tuple[11])
    patient_bmi_label = Label(pt_details_pt_view,text=patient_details_tuple[12])
    patient_allergies_label = Label(pt_details_pt_view,text=patient_details_tuple[13])
    patient_contact_label = Label(pt_details_pt_view,text=patient_details_tuple[14])
    patient_emer_contact_label = Label(pt_details_pt_view,text=patient_details_tuple[15])

    #setting grid position for labels
    welcome_text.grid(row=0,column=0)
    name_label.grid(row=0,column=1)
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



# def pt_details_staff_view(root_home,username):