'''
ALTER TABLE
    Alterar informação em uma tabela 
'''
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("alter table customers add column id int auto_increment primary key")