#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'dengjinyi'
import httplib2,MySQLdb,json
def yiqifaget(url):
    u='http://o.yiqifa.com/'+url
    http = httplib2.Http()
    resp, content=http.request(u,'GET')
    # print resp, content
    return resp, content
def getdata(strsql):
    conn=MySQLdb.connect('172.16.9.9','egou','egou','order',charset='utf8')
    cursor=conn.cursor()
    cursor.execute(strsql)
    data=cursor.fetchone()
    conn.close()
    return data
if __name__ == '__main__':
    url=r'servlet/productSearch?siteId=150&pageSize=1&userId=155&psw=123&eu_id=qqqq&productId=1353127257'
    resp,content=yiqifaget(url)
    print resp

