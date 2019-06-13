#!/usr/bin/env python
# encoding: utf-8
import httplib2,httplib
import json,sys,MySQLdb
sys.path.append("../common")
import yiqifaCommonMethod


def yiqifaProductEnv(url,type):
    resp,content=yiqifaCommonMethod.yiqifaproducthttps(url)
    # print resp
    if type == 'status':
        return resp['status']
        pass
    # return '200'
    pass
if __name__ == '__main__':

    h3 = httplib2.Http(".cache")
    h3.add_credentials('name', 'password')
    resp3, content3 = h3.request("https://221.122.127.184:19143/subject/shuang11",
    "GET",headers={'content-type':'text/plain'} )
    print resp3
    print content3
    # print resp
