#verificando existencia de tabela
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("show tables")

for x in mycursor:
    print(x)