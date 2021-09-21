'''
Para evitar problemas de uso indevido com o banco de dados, para a busca de um valor especifico deve-se utilizar "%s" na string de busca do banco de dados 
'''

import mysql.connector

mydb = mysql.connector.connect (
     host='localhost',
     user='root',
     password='12345',
     database='mydatabase'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"

adr= ("Yellow Garden 2",)

mycursor.execute(sql,adr)

myresult = mycursor.fetchall()

for x in myresult:
     print(x)