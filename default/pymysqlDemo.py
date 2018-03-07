# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-07 16:27
import pymysql as pymysql

db = pymysql.connect(host='localhost', user='root', password='admin', port=3306, db='spiders')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data1 = cursor.fetchone()
print('MySQL version: %s' % data1)

# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')


tableCreSql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(tableCreSql)

data1 = {
    'id': '04143130',
    'name': 'Charley',
    'age': 23
}
data2 = {
    'id': '04143133',
    'name': 'Kobe',
    'age': 24
}
data3 = {
    'id': '04143132',
    'name': 'None',
    'age': 21
}

table = 'students'
keys = ', '.join(data1.keys())
values = ', '.join(['%s'] * len(data1))

dataInsSql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)

print(dataInsSql)
try:
    if cursor.execute(dataInsSql, tuple(data1.values())) and cursor.execute(dataInsSql, tuple(data2.values())) and \
            cursor.execute(dataInsSql, tuple(data3.values())):
        print('Successful')
        db.commit()
except:
    print("Failed")
    db.rollback()

db.close()

