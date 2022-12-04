from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image
from time import time

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