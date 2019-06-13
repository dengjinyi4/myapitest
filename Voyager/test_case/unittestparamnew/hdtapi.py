#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib,random,xlrd,api_admin
import mydb
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
    s.get('https://apidisplay.adhudong.com/site_login_ijf.htm?app_key=adhub3dbfbcee89b4821&user_id=not_login&sign=4e2de116fe879d49064a2627616f08e1&referer=&user_fingerprint=d7549e04786505e858afd064117df888',verify=False)
    r=s.get(url,verify=False)
    print r.text
    return r.json()['code']
def actmethod(myurl):
    s=requests.session()
    s.get('https://apidisplay.adhudong.com/site_login_ijf.htm?app_key=adhub3dbfbcee89b4821&user_id=not_login&sign=4e2de116fe879d49064a2627616f08e1&referer=&user_fingerprint=d7549e04786505e858afd064117df888',verify=False)
    url='http://apidisplay.adhudong.com/phone_login_ijf.htm?adzone_id=101&media_id=55&phone=136'
    phone=random.randint(10000000, 99999999)
    url=url+str(phone)
    # print url
    x=s.get(url)
    # r=s.get("http://apidisplay.adhudong.com/sign.htm?act_id=32&adzoneId=101")
    r=s.get(myurl)
    print r.text
    return r.json()['code']
def getparam_excel():
    data=xlrd.open_workbook('test.xls')
    table = data.sheet_by_name(u'ok')
    myrows=table.nrows
    print myrows
    tmplist=[]
    tlist=[]
    for i in range(1,myrows):
        # print table.row_values(i)
        # tlist.append("(\"{0}\",\"{1}\")".format(table.row_values(i)[0],table.row_values(i)[1]))
        tlist.append((table.row_values(i)[0],table.row_values(i)[1],table.row_values(i)[2],table.row_values(i)[3]))
        # tmplist.append(tlist)
    # print tlist
    return tlist
def getparam_db(apiname):
    """

    :rtype : object
    """
    id =3
    testdb=mydb.mydb()
    # if apiname=='totalDetail':
    if id==1:
        tmpsql='SELECT testcasename,methodurl,param,expect_value,param_type from testcase where apiname='+"'"+apiname+"' and id="+id
        print tmpsql
        # tmpsql='SELECT testcasename,methodurl,param,expect_value,param_type from testcase where apiname=\'%s\''%apiname
    else:
        tmpsql='SELECT testcasename,methodurl,param,expect_value,param_type from testcase where apiname='+"'"+apiname+"'"
        print tmpsql

    # else:
    #     tmpsql='SELECT testcasename,param,expect_value,param_type from testcase where apiname='+"'"+apiname+"'"
    # # print tmpsql
    # print testdb.mydb_select(tmpsql)
    tmplist=[]
    try:
        for i in testdb.mydb_select(tmpsql):
            tmplist.append(i)
    except Exception , e:
        print e.message
    # print tmplist
    return tmplist
def initparam():
    s=api_admin.adminlogin()
    allcase=getparam_db('totalDetail')
    # print allcase
    tmplist=[]
    for i in allcase:
        tmpdup=()
        para=eval(i[2])
        result=s.get(str(i[1]),params=para)
        tmpdup=i[0],result.json()['code'],i[3],i[4],
        tmplist.append(tmpdup)
    # print tmplist
    return tmplist
if __name__ == '__main__':
    # s=api_admin.adminlogin()
    # print initparam()
    print  getparam_db('totalDetail')
