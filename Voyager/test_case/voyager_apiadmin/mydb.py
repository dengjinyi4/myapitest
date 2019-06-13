#!/usr/bin/env python
# encoding: utf-8
import MySQLdb as mysql
class mydb(object):
    def __init__(self):
        self.db=mysql.connect(host='221.122.127.183',user='voyager',passwd='voyager',db='test',port=5701,charset='utf8')
        # self.db.commit(True)
        self.cursor=self.db.cursor()
    def mydb_select(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result=self.cursor.fetchall()
            return result
        except Exception as e:
            print e
if __name__ == '__main__':
    testdb=mydb()
    tmpsql='SELECT testcasename,param,param_type,expect_value from test.testcase'
    print testdb.mydb_select(tmpsql)