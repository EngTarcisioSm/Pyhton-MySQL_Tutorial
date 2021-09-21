'''
Filtro where
     - Selecionando registros da tabela, filtrando itens com instrução where
'''
import mysql.connector

mydb = mysql.connector.connect (
     host='localhost',
     user='root',
     password='12345',
     database='mydatabase'
)

mycursor = mydb.cursor()

sql = "select * from customers where address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
     print(x)