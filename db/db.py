import sqlite3
import xlrd

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# create table cost_type
cursor.execute('drop table cost_type')
sql = 'create table cost_type(' \
      'c_id int primary key ,' \
      'type char(50) not null);'

cursor.execute(sql)

demo_file = 'demo.xlsx'
wb = xlrd.open_workbook(demo_file)

sheet1 = wb.sheet_by_index(0)
# 读取制造费用类型
cost_type = sheet1.col_values(2, 3, )
for i, t in enumerate(cost_type):
    t = t.strip()
    cursor.execute("insert into cost_type values(%d, '%s');" % (i, t))
conn.commit()
print([ct.strip() for ct in cost_type])
# create table real_output
cursor.execute('drop table real_output')
sql = 'create table real_output(' \
      't_id char(10) primary key,' \
      'output real not null );'
cursor.execute(sql)

# create table de_output
cursor.execute('drop table de_output')
sql = 'create table de_output(' \
      't_id char(10) primary key,' \
      'output real not null );'
cursor.execute(sql)

# create table real_cost
cursor.execute('drop table real_cost')
sql = 'create table real_cost(' \
      '_id integer primary key autoincrement, ' \
      'c_id integer not null,' \
      't_id char(10) not null,' \
      'cost real );'
cursor.execute(sql)

# create table de_cost
cursor.execute('drop table de_cost')
sql = 'create table de_cost(' \
      '_id integer primary key autoincrement, ' \
      'c_id integer not null,' \
      't_id char(10) not null,' \
      'cost real );'
cursor.execute(sql)

rt = ['20180812', '201901', '201902', '201903', '20190103', '201904', '201905', '201906', '20190406', '20190106']
tmp_cost = sheet1.row_values(3, 4, )
cost = []
for i, c in enumerate(tmp_cost):
      if i % 2 == 0:
            continue
      cost.append(c)

for t, c in zip(rt, cost):
      cursor.execute("insert into real_output values ('%s','%s');" % (t, c))
conn.commit()

for i in range(len(rt)):
      colx = 3 + 2 * i
      cost = sheet1.col_values(colx, 4, -2)
      for j, c in enumerate(cost):
            if c == 0 or c == '':
                  continue
            cursor.execute("insert into real_cost(c_id, t_id, cost) values (%d, '%s', %r)" % (j+1, rt[i], c))
conn.commit()

dt = ['20180812', '201901', '201902', '201903', '201904', '201905', '201906', '20190106']
sheet2 = wb.sheet_by_index(1)
tmp_cost = sheet2.row_values(3, 2, )
print(tmp_cost)
cost = []
for i, c in enumerate(tmp_cost):
      if i % 2 == 0:
            continue
      cost.append(c)

for t, c in zip(dt, cost):
      cursor.execute("insert into de_output values ('%s','%s');" % (t, c))
conn.commit()

for i in range(len(dt)):
      colx = 3 + 2 * i
      cost = sheet2.col_values(colx, 4, -2)
      for j, c in enumerate(cost):
            if c == 0 or c == '':
                  continue
            cursor.execute("insert into de_cost(c_id, t_id, cost) values (%d, '%s', %r)" % (j+1, dt[i], c))
conn.commit()
