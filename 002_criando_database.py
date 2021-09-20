import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345'
)

mycursor = mydb.cursor()
mycursor.execute("create database mydatabase")

#caso o banco ja exista, ocorrerá erro 