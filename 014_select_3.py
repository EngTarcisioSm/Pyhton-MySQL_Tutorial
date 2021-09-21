'''
buscar apenas uma unica linha
'''
import mysql.connector

mydb = mysql.connector.connect(
     host='localhost',
     user='root',
     password='12345',
     database='mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute('select * from customers')

myresult = mycursor.fetchone()

print(myresult)