#!/usr/bin/env python
#encoding: utf-8
import unittest,requests,sys

def ad_simulation(host):
    param={'adZoneId':1,'positionId':1,'bidTime':'2017-07-04'}
    url='http://'+host+'/ad_simulation.do?'
    # print url
    s=requests.session()
    r=s.get(url,params=param)
    print r.url
    count=len(r.json()['data']['1'])
    return count
def testbidding85(hostandport):
    	'''验证单台机器上123.59.17.85:17200模拟投放广告接口是否返回广告'''
        try:
            count=ad_simulation(hostandport)
        except:
            sys.exit(1)
        if count>0:
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ =='__main__':
    hostandport=sys.argv[1]
    testbidding85(hostandport)