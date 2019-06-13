#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib

def serviceUrl():
    url='''http://admin.adhudong.com:17071/'''
    return  url
# 后台登录
def login():
    param={'name':'test','pwd':'qq'}
    url=serviceUrl()+'login/login_in.htm?'
    print url
    s=requests.session()
    s.get(url,params=param)
    # print s
    # r=s.get('http://admin.adhudong.com:17071/user/ListUser.htm?username=coldman&status=1&descn=jack&create_time=1')
    return s

if __name__ == '__main__':
    login()
    print serviceUrl()
    
    
    
