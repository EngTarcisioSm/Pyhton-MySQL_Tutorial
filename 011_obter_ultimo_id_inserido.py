
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

sql = 'insert into customers (name, address) values (%s, %s)'
val = ('Michele', 'Blue Village')

mycursor.execute(sql, val)

mydb.commit()

print('1 record inserted, ID:', mycursor.lastrowid)

#caso executado mais de uma vez será inserido valor repetido 