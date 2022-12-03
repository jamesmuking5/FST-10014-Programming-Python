from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image

def patient_login(username,password): 
    #connect to mysql
    conn = mysql.connect(host="localhost",user="root",password="microsoft123")
        
    #create cursor
    cursor = conn.cursor()
        
    #check username via sql query
    sql_query_username = ("SELECT patient_ic FROM patient_signup.patient_login WHERE patient_ic = '"+username+"'")
    #execute cursor
    cursor.execute(sql_query_username)
    #fetch results
    username_result = cursor.fetchall()
        
    #check password via sql query
    sql_query_password = ("SELECT patient_password FROM patient_signup.patient_login WHERE patient_password = '"+password+"'")
    #execute cursor
    cursor.execute(sql_query_password)
    #fetch results
    password_result = cursor.fetchall()
    cursor.close()
    
    print(username)
    print(password)
    username_check = ("[('"+username+"',)]")
    print(username_check)
    password_check = ("[('"+password+"',)]")
    print(password_check)
    print(username_result)
    print(password_result)
        
    if str(username_check) == str(username_result) and str(password_check) == str(password_result):
        return TRUE
    else:
        return FALSE