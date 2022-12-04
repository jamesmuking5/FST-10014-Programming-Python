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

#Patient View
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
    welcome_text= Label(pt_details_pt_view, font=("Times",12), text="Patient details, "+full_name)
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
    patient_allergies_output= Label(pt_details_pt_view,text=patient_allergies)
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
    patient_allergies_output.grid(row=12,column=2)
    patient_contact_output.grid(row=13,column=2)
    patient_emer_contact_output.grid(row=14,column=2)

    def john():
        pt_details_pt_view.destroy()
        
    #Close button
    close_button_pt_details_pt_view = Button(pt_details_pt_view,text="Close",command=john,width=10).grid(row=15,column=1)

#Function for querying staff full name
def staff_details_collect(username):
    #connect to mysql
    conn = mysql.connect(host="localhost",user="root",password="microsoft123")
        
    #create cursor        
    cursor = conn.cursor()
        
    #define input variable        
    sql_access_staff_details = ("SELECT staff_full_name FROM patient_signup.staff_login WHERE staff_ic = '"+username+"'")
    cursor.execute(sql_access_staff_details)
    staff_details = cursor.fetchall()
    conn.commit()
    cursor.close()
    staff_details
    for x in staff_details:
        print(x)
    for name in x:
        return name
 
#Function for updating SQL on patient's details
def patient_check_right_wrong(pt_username):
    #connect to mysql
    conn = mysql.connect(host="localhost",user="root",password="microsoft123")
        
    #create cursor        
    cursor = conn.cursor()
        
    #define input variable        
    sql_access_patient_details = ("SELECT * FROM patient_signup.patient_login WHERE patient_ic = '"+pt_username+"'")
    cursor.execute(sql_access_patient_details)
    patient_name = cursor.fetchall()
    conn.commit()
    cursor.close()
    for x in patient_name:
        print(x)
    if pt_username in x:
        return TRUE
    else:
        return FALSE
    
#Staff View    
def pt_details_staff_view(root_home,username):
    pt_details_staff_view = Toplevel(root_home)
    pt_details_staff_view.title("MCB: Staff View")
    pt_details_staff_view.geometry("430x350")               
    
    #Search bar for patient's IC
    search_bar = Entry(pt_details_staff_view)
    search_bar.grid(row=1, column=0, columnspan=2)
    search_bar.insert(0,"Search Patient via I.C.")
    
    #creating labels
    welcome_text= Label(pt_details_staff_view, font=("Times",12), text="Search for patient details, "+staff_details_collect(username))
    name_label = Label(pt_details_staff_view,text="Patient's name:")
    blood_pressure_label = Label(pt_details_staff_view,text="Blood Pressure:")
    spiro_oxy_label = Label(pt_details_staff_view,text="SpO2:")
    heart_rate_label = Label(pt_details_staff_view,text="Heart Rate:")
    temperature_label = Label(pt_details_staff_view,text="Body Temperature:")
    current_disease_label = Label(pt_details_staff_view,text="Current Diseases:")
    medical_history_label = Label(pt_details_staff_view,text="Medical History:")
    patient_weight_label = Label(pt_details_staff_view,text="Recent Weight:")
    patient_height_label = Label(pt_details_staff_view,text="Recent Height:")
    patient_bmi_label = Label(pt_details_staff_view,text="Recent BMI:")
    patient_allergies_label = Label(pt_details_staff_view,text="Known Allergies:")
    patient_contact_label = Label(pt_details_staff_view,text="Patient Contact Num.:")
    patient_emer_contact_label = Label(pt_details_staff_view,text="Patient Emergency Contact Num.:")

    #setting grid position for labels
    welcome_text.grid(row=0,column=0,columnspan=3)
    name_label.grid(row=2,column=0)
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
    name_output = Entry(pt_details_staff_view)
    blood_pressure_output= Entry(pt_details_staff_view)
    spiro_oxy_output= Entry(pt_details_staff_view)
    heart_rate_output= Entry(pt_details_staff_view)
    temperature_output= Entry(pt_details_staff_view)
    current_disease_output= Entry(pt_details_staff_view)
    medical_history_output= Entry(pt_details_staff_view)
    patient_weight_output= Entry(pt_details_staff_view)
    patient_height_output= Entry(pt_details_staff_view)
    patient_bmi_output= Entry(pt_details_staff_view)
    patient_allergies_output= Entry(pt_details_staff_view)
    patient_contact_output= Entry(pt_details_staff_view)
    patient_emer_contact_output= Entry(pt_details_staff_view)
    
    #Position button grid
    name_output.grid(row=2,column=2)
    blood_pressure_output.grid(row=3,column=2)
    spiro_oxy_output.grid(row=4,column=2)
    heart_rate_output.grid(row=5,column=2)
    temperature_output.grid(row=6,column=2)
    current_disease_output.grid(row=7,column=2)
    medical_history_output.grid(row=8,column=2)
    patient_weight_output.grid(row=9,column=2)
    patient_height_output.grid(row=10,column=2)
    patient_bmi_output.grid(row=11,column=2)
    patient_allergies_output.grid(row=12,column=2)
    patient_contact_output.grid(row=13,column=2)
    patient_emer_contact_output.grid(row=14,column=2)
    
    #running SQL query in function to call patient database
    def retrieve_patient_data():
        pt_username = search_bar.get()
        weird_list_tuple = patient_details_collect(pt_username)
        print(weird_list_tuple) 
        for patient_details_tuple in weird_list_tuple:
            print(patient_details_tuple)
            name_output.delete(0, END)
            name_output.insert(0,patient_details_tuple[3])
            blood_pressure_output.delete(0, END)
            blood_pressure_output.insert(0,patient_details_tuple[4])
            spiro_oxy_output.delete(0, END)
            spiro_oxy_output.insert(0,patient_details_tuple[5])
            heart_rate_output.delete(0, END)
            heart_rate_output.insert(0,patient_details_tuple[6])
            temperature_output.delete(0, END)
            temperature_output.insert(0,patient_details_tuple[7])
            current_disease_output.delete(0, END)
            current_disease_output.insert(0,patient_details_tuple[8])
            medical_history_output.delete(0, END)
            medical_history_output.insert(0,patient_details_tuple[9])
            patient_weight_output.delete(0, END)
            patient_weight_output.insert(0,patient_details_tuple[10])
            patient_height_output.delete(0, END)
            patient_height_output.insert(0,patient_details_tuple[11])
            patient_bmi_output.delete(0, END)
            patient_bmi_output.insert(0,patient_details_tuple[12])
            patient_allergies_output.delete(0, END)
            patient_allergies_output.insert(0,patient_details_tuple[13])
            patient_contact_output.delete(0, END)
            patient_contact_output.insert(0,patient_details_tuple[14])
            patient_emer_contact_output.delete(0, END)
            patient_emer_contact_output.insert(0,patient_details_tuple[15])
            
    def push_update_patient_data():        
        #connect to mysql
        conn = mysql.connect(host="localhost",user="root",password="microsoft123")
        #create cursor        
        cursor = conn.cursor()
        #define input variable        
        sql_input_patient_data = ("UPDATE patient_signup.patient_login SET full_name='"+name_output.get()+"', blood_pressure='"+blood_pressure_output.get()+"', spo2='"+spiro_oxy_output.get()+"', heart_rate='"+heart_rate_output.get()+"', temperature='"+temperature_output.get()+"', current_diseases='"+current_disease_output.get()+"', medical_history='"+medical_history_output.get()+"', patient_weight='"+patient_weight_output.get()+"', patient_height='"+patient_height_output.get()+"', bmi='"+patient_bmi_output.get()+"', allergies='"+patient_allergies_output.get()+"', patient_contact='"+patient_contact_output.get()+"', patient_emergency='"+patient_emer_contact_output.get()+"' WHERE patient_ic='"+search_bar.get()+"'")
        
        print(search_bar.get())
        print(sql_input_patient_data)
        #execute data
        cursor.execute(sql_input_patient_data)
        conn.commit()
        cursor.close()
        return TRUE
                
    def update_patient_data():
        pt_username = search_bar.get()
        if patient_check_right_wrong(pt_username) == TRUE:
            if MessageBox.askyesno("Sure?","Are you sure you want to proceed?") == TRUE:
                if (push_update_patient_data()) == TRUE:
                    MessageBox.showinfo("Success.","The operation to update the patient's details was sucessful.")
                else:
                    MessageBox.showerror("Error","There was an error.")
            else:
                MessageBox.showinfo("Canceled.","Update canceled.")
        elif patient_check_right_wrong(pt_username) == FALSE:
            MessageBox.showerror("Error","Patient IC not found.")
        else:
            MessageBox.showerror("Oops.","This should not be happening.")

    def john():
        pt_details_staff_view.destroy()
       
    #Retrieve Patient Data
    retrieve_patient_data_button = Button(pt_details_staff_view, text="Retrieve",command=retrieve_patient_data,width=10).grid(row=1,column=2)
    #Update Patient Data
    update_patient_data_button = Button(pt_details_staff_view,text="Update",command=update_patient_data).grid(row=16,column=1)
    #Close button
    close_button_pt_details_staff_view = Button(pt_details_staff_view,text="Close",command=john,width=10).grid(row=16,column=3)