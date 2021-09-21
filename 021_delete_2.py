'''
É considerado uma boa prática escapar dos valores de qualquer consulta, também em instruções de exclusão.

Isso evita injeções de SQL, que é uma técnica comum de hacking para destruir ou usar indevidamente seu banco de dados.

O módulo mysql.connector usa o placeholder %spara escapar os valores na instrução delete:
'''
import mysql.connector

mydb = mysql.connector.connect (
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"

adr = ("Yellow Garden 2",)

mycursor.execute(sql,adr)

mydb.commit()

print(mycursor.rowcount, "records(s) deleted")