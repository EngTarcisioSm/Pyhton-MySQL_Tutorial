#criando uma tabela em um banco de dados 
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("create table customers (name varchar(255), address varchar(255))")

#caso a tabela ja exista será apresentado um erro 