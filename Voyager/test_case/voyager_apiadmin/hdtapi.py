#!/usr/bin/env python
# encoding: utf-8
import requests,random,json,sys,datetime
import test_case.voyager_apiadmin.api_admin as api_admin
from test_case.hdtapi_business.utils.common_log import *
from test_case.voyager_apiadmin import mydb


def getCmp_cases():
    '''获得汇总、媒体、广告报表同义字段对比的用例'''
    testdb = mydb.mydb()
    sql = '''SELECT id,testcasename,param,expect_value,param_type,`group`,apiname from testcase_adv where
                status=1 and apiState=1 and param_type='D' '''
    tmplist=[]
    try:
        for i in testdb.mydb_select(sql):
            tmplist.append(i)
    except Exception , e:
        print e.message
    return tmplist

def cmp_cases(days):
    logging.setLoggerClass(CommonLog)
    logger = logging.getLogger(__name__)
    admin_s = api_admin.adminlogin()
    logger.info('已经登录了，already login')
    logger.info('分别查询广告报表和汇总报表数据，获得广告消耗字段，进行对比')
    allcase = getCmp_cases()
    #id,testcasename,param,expect_value,param_type,`group`
    cases_data_list = []
    yestoday = (datetime.date.today() - datetime.timedelta(days=days)).strftime('%Y/%m/%d')
    for case in allcase:
        tmp = eval(case[2])
        url_counts=len(tmp)
        if case[5] in ('hdt_admin'):
            re=[]
            re_url = []
            #根据param，分别取到两个接口的广告消耗等数据
            for i in range(url_counts):
                result = admin_s.get(str(tmp[i]['url']).format(yestoday, yestoday))
                logger.info('id is ' + str(case[0]))
                logger.info(result.url)
                logger.info(result.text)
                logger.info('expect_value ' + case[3])
                values = result.json()['data']['data']
                re_url.append(result.url)
                if len(values) > 0:
                    re.append(values[0][tmp[i]['cmp_key']])
                else:
                    re.append(0)
            logger.info('汇总报表返回的广告消耗: '+ str(re[0]) + ',' + '广告报表返回的广告消耗是: ' + str(re[1]))
            # id,testcasename,param,expect_value,param_type,`group`,apiname
            code_data_tmp = str(case[0]) + '_' + str(case[1]) + '_', case[3], case[4], abs(int(re[0])-int(re[1])),case[6],re,re_url
            cases_data_list.append(code_data_tmp)
    return cases_data_list

if __name__ == '__main__':
    # s=api_admin.adminlogin()
    # adv = api_admin.adv_admin()
    del_gdatas()
    cmp_cases()
