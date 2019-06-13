# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 16:04
# @Author  : wanglanqing
import requests,random,json,sys,datetime
import logging
import MySQLdb as mysql
import test_case.voyager_apiadmin.api_admin as api_admin
from test_case.hdtapi_business.utils.common_log import *

class mydb(object):
    def __init__(self):
        self.db=mysql.connect(host='221.122.127.183',user='voyager',passwd='voyager',db='test',port=5701,charset='utf8')
        # self.db.commit(True)
        self.cursor=self.db.cursor()
    def mydb_select(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result=self.cursor.fetchall()
            return result
        except Exception as e:
            print e

def getparam_db(group='All'):
    """
    :rtype : object
    """
    testdb=mydb()
    if group== 'All':
        tmpsql = '''SELECT id,testcasename,methodurl,param,expect_value,param_type,remarks,actresult,`group` from testcase_adv where
                status=1 and apiState=1 and param_type in ('A','B','C');'''
    else:
        tmpsql = '''SELECT id,testcasename,methodurl,param,expect_value,param_type,remarks,actresult,`group` from testcase_adv where
            status=1 and apiState=1 and group={}  and param_type in ('A','B','C');'''.format(group)
    tmplist=[]
    try:
        for i in testdb.mydb_select(tmpsql):
            tmplist.append(i)
    except Exception , e:
        print e.message
    return tmplist

def del_gdatas():
    '''
    删除上一次自动化，遗留的测试数据
    :return:
    '''
    logging.setLoggerClass(CommonLog)
    logger = logging.getLogger(__name__)
    testdb = mydb()
    #定义sql中的变量
    ad_key_word = '用后删除的'
    aid = '2222455'
    #分别查询广告主订单、计划、创意ids
    order_ids = testdb.mydb_select("select id from voyager.ad_order ao where ao.name like '%{}%' and ao.advertiser_id='{}';".format(ad_key_word,aid))
    plan_id = testdb.mydb_select(" select id from voyager.ad_plan ap where ap.name like '%{}%' and ap.advertiser_id='{}';".format(ad_key_word,aid))
    creative_id = testdb.mydb_select("select id from voyager.ad_creative ac where ac.name like '%{}%' and ac.advertiser_id='{}';".format(ad_key_word,aid))
    #根据返回的ids值，删除历史数据
    if len(order_ids) > 0:
        for i in order_ids:
            # print ("delete from voyager.ad_order_creative aoc where aoc.order_ids in ({});".format(i[0]))
            logger.info("delete from voyager.ad_order_creative  where order_id in ({})".format(i[0]))
            logger.info("delete from  voyager.ad_order_direction  where order_id in ({})".format(i[0]))
            logger.info("delete from  voyager.ad_order  where id in ({})".format(i[0]))

            testdb.mydb_select("delete from voyager.ad_order_creative  where order_id in ({})".format(i[0]))
            testdb.mydb_select("delete from  voyager.ad_order_direction  where order_id in ({})".format(i[0]))
            testdb.mydb_select("delete from  voyager.ad_order  where id in ({})".format(i[0]))

    if len(plan_id)>0:
        for i in plan_id:
            logger.info( "delete from voyager.ad_plan where id in ({});".format(i[0]))
            testdb.mydb_select("delete from voyager.ad_plan where id in ({});".format(i[0]))

    if len(creative_id)>0:
        for i in creative_id:
            logger.info("delete from voyager.ad_creative_link where creative_id in ({});".format(i[0]))
            logger.info("delete from voyager.ad_creative where id in ({});".format(i[0]))
            testdb.mydb_select("delete from voyager.ad_creative_link where creative_id in ({});".format(i[0]))
            testdb.mydb_select("delete from voyager.ad_creative where id in ({});".format(i[0]))

def initparam():
    logging.setLoggerClass(CommonLog)
    logger = logging.getLogger(__name__)
    demand_s = api_admin.adv_admin()
    admin_s = api_admin.adminlogin()
    logger.info('已经登录了，already login')
    del_gdatas()
    logger.info('删除了历史测试数据')
    allcase = getparam_db()
    # logger.info('get allcase')
    cases_data_list = []

    for case in allcase:
        # logger.info(demand_s.cookies)
        logger.info('Start id is ' + str(case[0]))
        case_data = ()
        #判断是否有参数，如果有参数，则接口带参数请求；如果没有参数，则直接请求
        if case[8] in ('hdt_demand','hdt_ypg'):
            if case[3]:
                print case[1]
                para = eval(case[3])
                result = demand_s.get(str(case[2]), params=para)
                # print(result.url)
            else:
                result = demand_s.get(str(case[2]))
        elif case[8] in ('hdt_admin'):
            if case[3]:
                print case[1]
                para = eval(case[3])
                result = admin_s.get(str(case[2]), params=para)
                # print(result.url)
            else:
                result = admin_s.get(str(case[2]))
        else:
            pass
        #元组返回的固定值，返回用例（id）， 用例名称（testcasename），预期结果（expect_value），参数类型（param_type）
        code_data_tmp = str(case[0])+'_'+str(case[1])+'_'+str(case[6]), case[4], case[5],

        #根据不同的状态值，组织接口返回的实际结果
        code = result.json()['code']
        result_data = result.json()['data']
        logger.info(result.url)
        logger.info(result.text)
        logger.info('End expect_value ' + case[4])
        #返回500时，返回用例（id）+用例名称（testcasename）/预期结果（expect_value）/参数类型（param_type）/请求结果里返回的data部分，
        if code == 500:
            # case_data = str(case[0])+'_'+str(case[1])+':'+str(case[6]), result.json()['data'], case[4], case[5],
            case_data = code_data_tmp +  (result_data,)

        # 返回3,4时，返回用例（id）+用例名称（testcasename）/预期结果（expect_value）/参数类型（param_type）/请求结果里返回的data list里的第一个字段，
        elif code in (302,303,403,301) and case[5]=='A':
            # case_data = str(case[0]) + '_' + str(case[1])+':'+str(case[6]),  case[4], case[5],result.json()['data'][0],
            # if isinstance(result_data,list):
            case_data =code_data_tmp + (result_data[0],)
            # else:

        #返回200但data包含data时，返回id+testcasename、expect_value、param_type、code
        elif code in (200, ) and isinstance(result_data,dict) and result_data.has_key('data') and isinstance(result_data['data'], list) and len(result_data['data'])>0:
            case_data = code_data_tmp + (result_data['data'][0].keys(),)

        # elif code in (200,) and isinstance(result_data, dict) and result_data.has_key('data') and isinstance(result_data['data'][0], dict):
        #     case_data = code_data_tmp + (result_data['data'][0].keys(),)
            # 返回200但data包含data时，返回id+testcasename、expect_value、param_type、code

        # elif code in (200,) and isinstance(result_data, int):
        #     print code_data_tmp
        #     case_data = code_data_tmp + tuple(str(result_data))

        # 返回200时，返回用例（id）+用例名称（testcasename）/预期结果（expect_value）/参数类型（param_type）/请求结果里返回的data的keys，
        elif code in (200,) and result_data and case[5]=='B':
            # case_data = str(case[0]) + '_' + str(case[1]), result.json()['data'].keys(), case[4], case[5],
            case_data = code_data_tmp + (result_data.keys(),)

        #返回200但data为null时，返回id+testcasename、expect_value、param_type、code
        elif code in (200,302,303,403,301) and case[5]=='C':
            case_data = code_data_tmp + (code,)

        else:
            pass
        cases_data_list.append(case_data)
    return cases_data_list