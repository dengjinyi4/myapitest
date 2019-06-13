#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib,random,time,datetime
import re
from .mydb import *

def mydatetime():
    today=datetime.date.today()
    yesterday=today-datetime.timedelta(days=1)
    # mytime=time.strftime("%Y/%m/%d",(datetime.datetime.now()+datetime.timedelta(days=1)))
    tmp=str(yesterday).replace('-','/')
    tmp='datetime_eq_'+tmp
    return tmp
def adminlogin():
    myreq=requests.session()
    # myreq.get('http://api.admin.adhudong.com/login/login_in.htm?name=aidinghua&pwd=!Adh1987',verify=False)
    myreq.get('http://api.admin.adhudong.com/login/login_in.htm?name=dengjinyi&pwd=!Aa123456',verify=False)
    return myreq
# 汇总报表

def adv_admin():
    '''
    广告主前台账号登录
    :return:
    '''
    advlogin = requests.session()
    db = mydb()
    requests.get('https://apidemand.adhudong.com/api/phone/sendAgentLoginCode.htm?name=advagent&phone=13815467894')
    tmp_code = db.mydb_select('''SELECT MSG FROM voyager.`phone_send_record` where phone='13815467894' order by id desc limit 1;''')
    pattern = re.compile(r'\d+')
    phone_code = str(pattern.findall(tmp_code[0][0])[0])
    res = advlogin.get('http://api.demand.adhudong.com/api/advert/login.htm?name=advagent&password=qq123456&phone=13815467894&phone_code={}'.format(phone_code))
    print res.url
    print res
    return advlogin

def totalDetail():
    r=adminlogin()
    mydate=mydatetime()
    para={'dateBegin':mydate,'dateEnd':mydate,'page':1,'page_size':100}
    result=r.get('http://api.admin.adhudong.com/report/totalDetail.htm',params=para)
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
    print adv_admin()
