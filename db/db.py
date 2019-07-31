import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

# sql = 'create table login (id varchar(20) primary key, name varchar(30), password varchar(30))'
# cursor.execute(sql)



