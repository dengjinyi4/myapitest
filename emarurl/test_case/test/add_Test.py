#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
def add(a):
    if (a==2):
        return 3
    return a
def getdata(strsql):
    db=MySQLdb.connect('172.16.9.9','egou','egou','order')
    cursor=db.cursor()
    # cursor.execute('SELECT * from user_order_0 LIMIT 2 ')
    cursor.execute(strsql)
    data=cursor.fetchone()
    db.close()
    return data
def updatedata(strsql):
    db=MySQLdb.connect('172.16.9.9','egou','egou','order')
    cursor=db.cursor()
    cursor.execute('UPDATE user_order_0 SET PRICE=9.99 WHERE id =1')
    db.commit()
    cursor.execute('SELECT * from user_order_0  WHERE id =1 ')
    data=cursor.fetchone()
    print data[11]
    db.close()
if __name__ == '__main__':
    sql='SELECT * from user_order_0 LIMIT 2'
    data=getdata(sql)
    print data[5]




