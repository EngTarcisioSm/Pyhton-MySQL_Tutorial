'''
Selecionar determinadas colunas
'''
import mysql.connector

mydb = mysql.connector.connect (
     host='localhost',
     user='root',
     password='12345', 
     database='mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("select name address from customers")

myresult = mycursor.fetchall()

for x in myresult:
     print(x)