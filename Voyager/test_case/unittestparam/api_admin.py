#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib,random,time,datetime
def mydatetime():
    today=datetime.date.today()
    yesterday=today-datetime.timedelta(days=1)
    # mytime=time.strftime("%Y/%m/%d",(datetime.datetime.now()+datetime.timedelta(days=1)))
    tmp=str(yesterday).replace('-','/')
    tmp='datetime_eq_'+tmp
    return tmp
def adminlogin():
    myreq=requests.session()
    result=myreq.get('http://api.admin.adhudong.com/login/login_in.htm?name=dengjinyi&pwd=!Ww123456',verify=False)
    print result.text
    return myreq
# 汇总报表
def totalDetail():
    r=adminlogin()
    mydate=mydatetime()
    para={'dateBegin':mydate,'dateEnd':mydate,'page':1,'page_size':100}
    result=r.get('http://api.admin.adhudong.com/report/totalDetail.htm',params=para)
    print result.url
    print result.json()
    # print result.status_code
    return result.json()['code']
# 媒体报表
def reportZone():
    r=adminlogin()
    mydate=mydatetime()
    para={'order_by':'a.date DESC','date_begin':mydate,'date_end':mydate,'page':1,'page_size':100}
    result=r.get('http://api.admin.adhudong.com/reportdaily/reportZone.htm',params=para)
    return result.json()['code']
# 广告报表
def reportOrder():
    r=adminlogin()
    mydate=mydatetime()
    para={'order_by':'a.date DESC','date_begin':mydate,'date_end':mydate,'page':1,'page_size':100}
    result=r.get('http://api.admin.adhudong.com/reportdaily/reportOrder.htm',params=para)
    # print result.text
    return result.json()['code']
# 经营分析报表
def reportDay():
    r=adminlogin()
    mydate=mydatetime()
    para={'order_by':'a.date DESC','date_begin':mydate,'date_end':mydate,'page':1,'page_size':100}
    result=r.get('http://api.admin.adhudong.com/reportdaily/reportDay.htm',params=para)
    print result.text
    return result.json()['code']
if __name__ == '__main__':
    print adminlogin()
