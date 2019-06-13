# -*- coding: UTF-8 -*-

import sys
import MySQLdb
import datetime
def mydb():
  db = MySQLdb.connect(host='123.59.17.121',user='voyager',passwd='SIkxiJI5r48JIvPh',db='voyager',port=3306,charset='utf8')
  db.autocommit(True)
  return db
def myselect(tsql):
  db=mydb()
  c=db.cursor()
  c.execute(tsql)
  result=c.fetchall()
  for i in result:
    re=int(i[0])
  return re
def tmpdaylist(days):
  daylist=''
  d = datetime.datetime.now()
  tmpdate_from=d+datetime.timedelta(days=-int(days))
  tmpdate_from=str(tmpdate_from)[0:10].replace('-','')
  daylist=tmpdate_from
  return daylist
def tmpsql(logid):
  mydata=tmpdaylist(0)
  tmpsql=[]
  ad_click_log="SELECT count(1) FROM voyagerlog.ad_click_log"+mydata+" where adzone_click_id ='"+logid+"'"
  ad_show_log="SELECT count(1) FROM voyagerlog.ad_show_log"+mydata+" where adzone_click_id ='"+logid+"'"
  adzone_click_log="SELECT count(1) FROM voyagerlog.adzone_click_log"+mydata+" where adzone_click_id ='"+logid+"'"
  lottery_click_log="SELECT count(1) FROM voyagerlog.lottery_click_log"+mydata+" where adzone_click_id ='"+logid+"'"
  tmpsql.append(ad_click_log)
  tmpsql.append(ad_show_log)
  tmpsql.append(adzone_click_log)
  tmpsql.append(lottery_click_log)
  # print tmpsql
  return tmpsql
def mydriverpath():
    #tmp='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    tmp='C:\Users\yiqifaqa\AppData\Local\Google\Chrome\Application\\chromedriver.exe'
    return tmp
