#conectar a um banco de dados mysql
import mysql.connector

'''atributo databse recebe nome do banco de dados a serem acessado'''

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase' 
)