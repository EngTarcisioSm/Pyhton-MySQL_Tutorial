#verificando a existencia de um banco de dados 
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345'
)

mycursor = mydb.cursor()

mycursor.execute("show databases")

for x in mycursor:
    print(x)