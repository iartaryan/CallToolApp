#!/usr/local/bin/python3
# coding=utf-8
import pymysql

db = pymysql.connect(host=, user=, passwd=, db=, port=)

cursor = db.cursor()

cursor.execute('SELECT src,calldate FROM cdr')# WHERE calldate > ' + '"' +str(time_1min)+'"')

data_1 = cursor.fetchall()

for i in data_1:
    print(i)



