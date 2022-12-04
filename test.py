from tkinter import *
import tkinter.messagebox as MessageBox
from mysql import *
import mysql.connector as mysql
from PIL import ImageTk,Image
from time import time

root_home = Tk()
from patient_details import *
print(patient_details_collect("user123"))
a = patient_details_collect("user123")
for x in a:
    miao = x
full_name = miao[3]
print(full_name)

mainloop()