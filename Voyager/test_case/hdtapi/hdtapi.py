#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib,random
# 模拟投放
def ad_simulation(host):
    param={'adZoneId':1,'positionId':1,'bidTime':'2017-07-04'}
    url='http://'+host+'/ad_simulation.do?'
    print url
    s=requests.session()
    r=s.get(url,params=param)
    print len(r.json()['data']['1'])
    # r=s.get('http://admin.adhudong.com:17071/user/ListUser.htm?username=coldman&status=1&descn=jack&create_time=1')
    return r
# 返回奖品列表
def allmethod(url):
    # url='https://apidisplay.adhudong.com/notice/list.htm?adzoneId=101&act_id=166'
    s=requests.session()
    s.get('https://apidisplay.adhudong.com/site_login_ijf.htm?app_key=adhu167db58761014193',verify=False)
    r=s.get(url,verify=False)
    print r.text
    return r.json()['code']
def actmethod(myurl):
    s=requests.session()
    s.get('https://apidisplay.adhudong.com/site_login_ijf.htm?app_key=adhu167db58761014193',verify=False)
    url='http://apidisplay.adhudong.com/phone_login_ijf.htm?adzone_id=101&media_id=55&phone=13641361201'
    phone=random.randint(10000000, 99999999)
    url=url+str(phone)
    # print url
    x=s.get(url)
    # r=s.get("http://apidisplay.adhudong.com/sign.htm?act_id=32&adzoneId=101")
    r=s.get(myurl)
    print r.text
    return r.json()['code']
if __name__ == '__main__':
    # ad_simulation('123.59.17.85:17200')
    # url='http://apidisplay.adhudong.com/sign.htm?act_id=32&adzoneId=101'
    # actmethod(url)
    url='http://apidisplay.adhudong.com/phone_login_ijf.htm?adzone_id=101&media_id=55&phone=136'
    phone=random.randint(10000000, 99999999)
    url=url+str(phone)
    print url

    # print r.text
