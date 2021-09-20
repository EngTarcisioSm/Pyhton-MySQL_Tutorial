'''
Chave primária
Ao criar uma tabela, você também deve criar uma coluna com uma chave exclusiva para cada registro.

Isso pode ser feito definindo uma CHAVE PRIMÁRIA.

Usamos a instrução "INT AUTO_INCREMENT PRIMARY KEY" que irá inserir um número único para cada registro. Começando em 1 e aumentado em um para cada registro.
'''

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("create table customers2 (id int auto_increment primary key, name varchar(255), address varchar(255))")