'''
É possivel selecionar registros que comecem ou terminem ou tenham no meio de seu texto determinada letra ou string
     - xyz%    :registros que comecem com xyz
     - %abc    :registros que terminem com abc
     - %abc%   :registros que tenham no meio de seu texto abc
'''
import mysql.connector

mydb = mysql.connector.connect (
     host='localhost',
     user='root',
     password='12345',
     database='mydatabase'
)

mycursor = mydb.cursor()

sql = "select * from customers where address like '%way%'"  # like utilizado para auxilio do filtro 'como'

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
     print(x)