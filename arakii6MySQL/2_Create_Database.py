# Connecting to MySql using Python
# To confirm connection, print out the connection id
import 1_Connect


# Create a New Database
cur = mydb.cursor()
cur.execute("CREATE DATABASE db1")