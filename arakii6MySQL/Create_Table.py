import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'admin',
    database = 'db1')
print(mydb.connection_id)



# Create a New Database
cur = mydb.cursor()
T = "CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(T)