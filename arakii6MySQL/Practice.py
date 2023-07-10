import mysql.connector
testdb = mysql.connector.connect(host = 'localhost',
                                 user = 'root',
                                 password = 'admin',
                                 database = 'testdb')

testcur = testdb.cursor()
'''testcur.execute("create database testdb")
testcur.execute("create table testtable(c1 integer(3),c2 varchar(5),c3 integer(3))")
coloums = [(1,"test1",101),(2,"test1",102),(3,"test1",103),(4,"test1",104),(5,"test1",105)]
for c in coloums:
    testcur.execute("insert into testtable(c1,c2,c3) VALUES(%s,%s,%s)",c)
testdb.commit()
coloums = [(6,"test1",106),(7,"test1",107),(8,"test1",108),(9,"test1",109),(10,"test1",111)]
testcur.executemany('insert into testtable(c1,c2,c3) values(%s,%s,%s)',coloums)
testdb.commit()'''

testcur.execute("update testtable set c3 = 110 where c1 = 10")
testdb.commit()

