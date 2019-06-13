#!/usr/bin/env python
# encoding: utf-8
import MySQLdb as mysql
class mydb(object):
    def __init__(self):
        self.db=mysql.connect(host='127.0.0.1',user='test',passwd='test',db='test',port=3306,charset='utf8')
        # self.db.commit(True)
        self.cursor=self.db.cursor()
    def mydb_select(self,sql):
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            return result
        except Exception as e:
            print e
if __name__ == '__main__':
    testdb=mydb()
    tmpsql='SELECT testcasename,param,param_type,expect_value from testcase'
    print testdb.mydb_select(tmpsql)