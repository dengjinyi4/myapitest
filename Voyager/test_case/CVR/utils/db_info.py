# encoding=utf-8
__author__ = 'aidinghua'
import MySQLdb as mysql

class DbOperation(object):

    def __init__(self,env_value):

        if env_value == True:

            self.db=mysql.connect(host='221.122.127.183',port=5701,db='voyager',user='voyager',passwd='voyager',charset = 'utf8')

        else:
            self.db=mysql.connnect(host='123.59.17.121',port=3306,db='voyager',user='voyager',passwd='SIkxiJI5r48JIvPh',charset = 'utf8')

        self.cursor=self.db.cursor()

    def excute_sql(self,sql):

        print "执行的sql是:"+sql
        try:
         self.cursor.execute(sql)
         self.db.commit()
         result=self.cursor.fetchall()
         return result[0][0]


        except Exception as e :
            print e
    def excute_sql1(self,sql):

        print "执行的sql是:"+sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result=self.cursor.fetchall()
            return result[0]


        except Exception as e :
            print e
    def delete_sql(self,sql):

        print "执行的sql是:"+sql
        try:
            self.cursor.execute(sql)
            self.db.commit()



        except Exception as e :
            print e

    def close_db(self):

        self.db.close()

    def close_cursor(self):

        self.cursor.close()

    def mycommit(self):

        self.db.commit()

    def myrollback(self):

        self.db.rollback()




if __name__=='__main__':

    mydb=DbOperation(True)
    sql="select id from voyager.template_type where name='类型1'"
    re=mydb.excute_sql(sql)
    print re

