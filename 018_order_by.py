'''
ORDER BY
    - USADO PARA CLASSIFICAR O RESULTADO EM ORDEM CRESCENTE OU DECRESCENTE
    - POR PADRÃO A ORGANIZAÇÃO SE DA EM OPRDEM CRESCENTE 
    - PARA ORGANIZAR EM ORDEM DECRESCENTE UTILIZAR AO FINAL A PALAVRA DESC
'''
import mysql.connector

mydb = mysql.connector.connect (
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

sql= "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)