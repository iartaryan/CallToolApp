#!/usr/local/bin/python3
# coding=utf-8
import pymysql

db = pymysql.connect(host='172.24.177.98', user='root', passwd='some_pass', db='asteriskcdrdb', port=3306)

cursor = db.cursor()

cursor.execute('SELECT src,calldate FROM cdr')# WHERE calldate > ' + '"' +str(time_1min)+'"')

data_1 = cursor.fetchall()

for i in data_1:
    print(i)



