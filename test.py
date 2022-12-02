import mysql.connector
conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "demanzJ_17",
        database = "patient_signup"
)

if conn.is_connected:
        print("Connection successful")