from Config import mydb
from Config import cur

cur.execute('select * from book')
result = cur.fetchall()

for r in result:
    print(r)