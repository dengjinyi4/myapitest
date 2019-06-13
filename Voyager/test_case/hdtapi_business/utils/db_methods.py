# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 9:53
# @Author  : wanglanqing


from test_case.hdtapi_business.test_data.db_data import *
import MySQLdb

class DbOperations(object):

    def __init__(self):
        self.db = MySQLdb.connect(host=db_data['host'],
                                   port=db_data['port'],
                                   db=db_data['db'],
                                   user=db_data['user'],
                                   passwd=db_data['password'],
                                   # charset=db_data['charset']),
                                   charset = 'utf8')
        self.cursor = self.db.cursor()

    def execute_select_sql(self, sql):
        print '执行的sql是： '+ sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
            results = self.cursor.fetchall()
            print 'sql执行的结果是： ' , results
            return results
        except Exception as e:
            print e

    def len_value(self, sql):
        print '执行的sql是： '+ sql
        results = self.execute_select_sql(sql)
        if results == None:
            results = 0
            return results
        else:
            return len(results)
        sum()


    def close_db(self):
        self.db.close()

    def close_cursor(self):
        self.cursor.close()

if __name__=='__main__':
    db = DbOperations()
    sql= "select * from voyagerlog.adzone_click_log20171214 WHERE act_id=1 and adzone_id=109 and media_id=40 and adzone_click_id='B3W1CD6H1HN01S2WBL'"
    db.execute_select_sql(sql)
