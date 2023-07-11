from Config import mydb
from Config import cur
from Config import result

cur.execute("update book set price = price + 10 where price < 50")
mydb.commit()