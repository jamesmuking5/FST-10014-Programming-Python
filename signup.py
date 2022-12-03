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