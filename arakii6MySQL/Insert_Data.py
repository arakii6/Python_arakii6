# Connecting to MySql & Selecting the Database
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'admin',
    database = 'db1')

# Inserting Data into Table
cur = mydb.cursor()
I = "INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"                     

while True:
    Data_Entry = input("To enter data press E, to quit press Q: ")
    
    if Data_Entry == 'E':
        bookid = int(input("Enter Book Id: "))
        title = input("Enter Book Name: ")
        price = float(input("Enter Price: "))
    
    elif Data_Entry == 'Q':
        break

book_data = (bookid,title,price)
cur.execute(I,book_data)
mydb.commit()