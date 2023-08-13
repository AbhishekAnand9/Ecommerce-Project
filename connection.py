import mysql.connector

def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin",
        database="ecommercedb"  
    )
def db_cursor(connection):
    return connection.cursor()

mydb = db_connection()
mycursor =db_cursor(mydb)

def Dbconnect():
    mycursor = mydb.cursor()
    return mycursor
    
def disConnectDb():
    mydb.close()
    