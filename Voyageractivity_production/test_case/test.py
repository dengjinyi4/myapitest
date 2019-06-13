#!/usr/bin/env python
#encoding: utf-8
import sys,time
reload(sys)  
sys.setdefaultencoding('utf8')   
import requests
# re=requests.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.16&destip=123.59.17.85')
# # re=requests.get('http://172.16.106.12:3333/jsontest/')
# print re.text
# print re.json()['code']
# print type(str(re.text))
# url='https://display.adhudong.com/new/draw_card.html?logId=B0H2YDC01HNKCU4BC1&adzoneId=270&actId=21&ref=&mediaId=2'
# print url[54:72]
# tmptime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# tmptime=time.strftime("%Y-%m-%d-%H:%M", time.localtime())
# print type(tmptime)
# print "运行时间是:%skklkj"%tmptime
def add(x,y):
    return x+y
if __name__ == '__main__':
    print add(1,3)
