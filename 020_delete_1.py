'''
É possivel excluir registros de uma tabela existente usando a instrução "DELETE FROM"

A declaração mydb.commit() é necessário fazer para que a alteração ocorra 

A clausula where especifica quais registros devem ser excluidos. Caso o where seja omitido, todos os registros serão excluidos 
'''
import mysql.connector

mydb = mysql.connector.connect (
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'record(s) deleted')