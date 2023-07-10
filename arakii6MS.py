# Connecting to MySql using Python
# To confirm connection, print out the connection id
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin')
print(mydb.connection_id)


# Create a New Database
cur = mydb.cursor()
cur.execute("CREATE DATABASE db1")