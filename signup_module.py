from tkinter import * 
import mysql.connector as mysql

def login(username_entry,password_entry):
    username = "root"
    password = "microsoft123"

    # connect to mysql
    conn = mysql.connect(
        host="localhost",
        user=username,
        passwd=password
    )

    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()
    print("Database version : %s " % data)
    
    #execute sql query
    print(username_entry)
    print(password_entry)
    stringvar = str(username_entry)
    var1 = ("SELECT * FROM patient_signup.patient_login WHERE IC_number = " + stringvar)
    cursor.execute(var1)
    
    #Fetch data
    fetched_data = cursor.fetchall()
    
    #print data
    print(fetched_data)