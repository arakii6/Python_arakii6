from Config import mydb
from Config import cur

cur.execute('delete from book where price < 50')
mydb.commit()