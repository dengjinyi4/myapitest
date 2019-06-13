#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time,random,datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import  pymssql
def con():
    con=pymssql.connect(host='127.0.0.1',user='sa',password='nopass.2',database='kaoqin',charset="utf8")
    return con
    pass
def sqlworkday(today,month):
    # 获得工作日的日期
    sql='''SELECT  CONVERT(char(10),CHECKTIME,120) d FROM CHECKINOUT where CHECKTIME<='%s' and CHECKTIME>'%s'
    group BY CONVERT(char(10),CHECKTIME,120)
    having  COUNT(*)>50
    ORDER BY  CONVERT(char(10),CHECKTIME,120)
    '''%(today,month)
    print 'workdaysql is %s\n'%sql
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
    t=day
    # checkin
    tmpminute=str(random.randint(0,30))
    tmpsecond=str(random.randint(10,59))
    t1=t+' 08:'+tmpminute+':'+tmpsecond
    # checkout
    tmpminute=str(random.randint(0,10))
    tmpsecond=str(random.randint(10,59))
    t2=t+' 17:'+tmpminute+':'+tmpsecond
    return str(t1),str(t2)
    pass
def writelog(gettime):
    f=open('1.txt','a')
    f.writelines('\n签到时间：'+gettime)
    f.close()
    pass
def instersql(userid,checkinday,checkoutday):
    tmpshangbansql='INSERT into  [kaoqin].[dbo].[CHECKINOUT] (USERID,CHECKTIME,CHECKTYPE,VERIFYCODE,SENSORID,Memoinfo,WorkCode,sn,UserExtFmt) VALUES (%s,\'%s\',\'I\',1,102,null,0,\'3399162100924\',1)'%(userid,checkinday)
    tmpxiabansql='INSERT into [kaoqin].[dbo].[CHECKINOUT] (USERID,CHECKTIME,CHECKTYPE,VERIFYCODE,SENSORID,Memoinfo,WorkCode,sn,UserExtFmt) VALUES (%s,\'%s\',\'I\',1,102,null,0,\'3399162100924\',1)'%(userid,checkoutday)
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
    # print '工作日\n%s'%workday
    for d in  workday:
        print sqldel(d,6)
        print '\n插入数据'
        # print type(d)
        tin,tout=getchkintime(d[0])
        # print '开始结束时间：%s '%tin
        # print instersql(tin,tout)[0]
def writelognew(workday,delsql,insql,outsql):
    f=open('2.txt','a')
    f.writelines('\n--workday：%s--'%workday)
    f.writelines('\n--delsql:--\n'+delsql)
    f.writelines('\n--checkinsql:--\n'+insql)
    f.writelines('\n--checkoutsql:--\n'+outsql)
    f.close()
    pass

if __name__ == '__main__':
    sqlwork=sqlworkday(datetime.date.today(),datetime.date.today().replace(day=1))
    workday=execselect(sqlwork)
    workday.sort()
    userid=264
    for d in  workday:
        print '-----开始---------\n---工作日是：%s\n---删除数据是'%str(d[0])
        print sqldel(d[0],userid)
        intime,outtime=getchkintime(d[0])
        print instersql(userid,intime,outtime)[0]+'\n'
        print instersql(userid,intime,outtime)[1]
        writelognew(str(d[0]),str(sqldel(d[0],userid)),str(instersql(userid,intime,outtime)[0]),instersql(userid,intime,outtime)[1])
        print '-------结束-----------'