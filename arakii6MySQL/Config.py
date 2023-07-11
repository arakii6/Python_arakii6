import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'admin',
    database = 'db1')

cur = mydb.cursor()
cur.execute('select * from book')
result = cur.fetchall()