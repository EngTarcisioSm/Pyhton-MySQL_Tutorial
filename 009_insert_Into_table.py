'''
    - Para preencher uma tablea no mysql, usa-se a instrução "insert into"
    - Observe a declaração: mydb.commit(). É necessário fazer as alterações, caso contrário, nenhuma alteração será feita na tabela.
'''
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

sql = "insert into customers (name, address) values (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record insert")