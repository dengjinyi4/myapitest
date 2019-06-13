#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time,random,datetime
import  pymssql
def con():
    con=pymssql.connect(host='127.0.0.1',user='sa',password='nopass.2',database='kaoqin',charset="utf8")
    return con
    pass
def sqlworkday(today,month):
    # 获得工作日的日期
    sql='''SELECT  CONVERT(char(10),CHECKTIME,120) d FROM CHECKINOUT where CHECKTIME<='%s' and CHECKTIME>%s
    group BY CONVERT(char(10),CHECKTIME,120)
    having  COUNT(*)>50
    ORDER BY  CONVERT(char(10),CHECKTIME,120)
    '''%(today,month)
    return sql
    pass
def sqldel(day,usid):
    # 删除数据
    sql='''delete from CHECKINOUT where CONVERT(char(10),CHECKTIME,120)='%s' and userid=%s'''%(day,usid)
    return sql
    pass

def execselect(sql):
    con1=con()
    cur=con1.cursor()
    if not cur:
        print 'DB not con'
    cur.execute(sql.encode('utf8'))
    reslist=cur.fetchall()
    con1.close()
    return reslist
    pass

def gettoday():
    # t1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    t1=datetime.date.today()
    return t1
    pass
def getchkintime(day):
    t1=day
    # checkin
    tmpminute=str(random.randint(0,30))
    tmpsecond=str(random.randint(10,59))
    t1=t1+' 08:'+tmpminute+':'+tmpsecond
    # checkout
    tmpminute=str(random.randint(0,10))
    tmpsecond=str(random.randint(10,59))
    t2=t1+' 17:'+tmpminute+':'+tmpsecond
    return str(t1),str(t2)
    pass
def writelog(gettime):
    f=open('1.txt','a')
    f.writelines('\n签到时间：'+gettime)
    f.close()
    pass
def instersql(checkinday,checkout):
    tmpshangbansql='INSERT into CHECKINOUT (USERID,CHECKTIME,CHECKTYPE,VERIFYCODE,SENSORID,Memoinfo,WorkCode,sn,UserExtFmt) VALUES (6,\'%s\',\'%s\',1,102,,0,\'3399162100924\',1)'%checkinday
    tmpxiabansql='INSERT into CHECKINOUT (USERID,CHECKTIME,CHECKTYPE,VERIFYCODE,SENSORID,Memoinfo,WorkCode,sn,UserExtFmt) VALUES (6,\'%s\',\'%s\',1,102,,0,\'3399162100924\',1)'%checkout
    return tmpshangbansql,tmpxiabansql
    pass
def getsql(userid,checktime):
    tmpsql='select * from CHECKINOUT where userid=%s and CHECKTIME>%s'%(userid,checktime)
    return tmpsql
    pass
def printsql():
    sqlwork=sqlworkday(datetime.date.today(),datetime.date.today().replace(day=1))
    print sqlwork
    workday=execselect(sqlwork)
    print '工作日\n%s'%workday
    for d in  workday:
        print sqldel(d,6)
        print '\n插入数据'
        # print type(d)
        tin,tout=getchkintime(d[0])
        # print '开始结束时间：%s '%tin
        # print instersql(tin,tout)[0]
if __name__ == '__main__':
    workday=[(u'2016-09-12',), (u'2016-09-13',), (u'2016-09-14',), (u'2016-09-19',), (u'2016-09-20',), (u'2016-09-21',), (u'2016-09-23',), (u'2016-09-26',), (u'2016-09-28',), (u'2016-09-29',), (u'2016-10-08',), (u'2016-10-09',), (u'2016-10-10',), (u'2016-10-11',), (u'2016-10-12',), (u'2016-10-13',), (u'2016-10-14',), (u'2016-10-17',), (u'2016-10-18',), (u'2016-10-19',)]
    sqlwork=sqlworkday(datetime.date.today(),datetime.date.today().replace(day=1))
    print sqlwork
    # workday=execselect(sqlwork)
    print workday[0][0]
    print type(workday)
    print '工作日\n%s'%workday
    for d in  workday:
        print str(d[0])
        print sqldel(d[0],6)


