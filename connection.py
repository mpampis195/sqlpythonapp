import mysql.connector 

def get_connection():
    return mysql.connector.connect (
    host = "localhost",
    user="root",
    password="",
    database="student",
    port =3306
  )