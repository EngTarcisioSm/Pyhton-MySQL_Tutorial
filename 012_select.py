'''
Instrução SELECT 
    - selecionar dados, todos dados da tabela 
'''
import mysql.connector

mydb = mysql.connector.connect (
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("select * from customers")

myresult = mycursor.fetchall()      # fetchall busca todas as linhas da ultima instrução executada.

for x in myresult:
    print(x)