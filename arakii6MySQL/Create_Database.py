# Import mydb variable from Connect
from Connect import mydb

# Create a New Database
cur = mydb.cursor()
cur.execute("CREATE DATABASE db1")