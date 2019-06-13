#!/usr/bin/env python
# encoding: utf-8
import requests,random,json,sys,datetime
import logging
# from test_case.voyager_apiadmin.api_admin  import *
import test_case.voyager_apiadmin.api_admin as api_admin
from test_case.hdtapi_business.utils.common_log import *
    # ,urllib,json,hashlib,,xlrd,
import mydb
# 模拟投放
reload(sys)
sys.setdefaultencoding('utf8')
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
def getparam_db(group='All'):
    """
    :rtype : object
    """
    testdb=mydb.mydb()
    # if apiname=='totalDetail':
    # tmpsql='SELECT id,testcasename,methodurl,param,expect_value,param_type from testcase where status=1 and apiname='+"'"+apiname+"'"
    if group== 'All':
        tmpsql = '''SELECT id,testcasename,methodurl,param,expect_value,param_type,remarks,actresult,`group` from testcase_adv where
                status=1 and apiState=1 and param_type in ('A','B','C');'''
    else:
        tmpsql = '''SELECT id,testcasename,methodurl,param,expect_value,param_type,remarks,actresult,`group` from testcase_adv where
            status=1 and apiState=1 and group={}  and param_type in ('A','B','C');'''.format(group)

    # -- and actresult=200
    # else:
    #     tmpsql='SELECT testcasename,param,expect_value,param_type from testcase where apiname='+"'"+apiname+"'"
    # print tmpsql
    # print testdb.mydb_select(tmpsql)
    tmplist=[]
    try:
        for i in testdb.mydb_select(tmpsql):
            tmplist.append(i)
    except Exception , e:
        print e.message
    return tmplist

def getCmp_cases():
    testdb = mydb.mydb()
    sql = '''SELECT id,testcasename,param,expect_value,param_type,`group` from testcase_adv where
                status=1 and apiState=1 and param_type='D' '''
    tmplist=[]
    try:
        for i in testdb.mydb_select(sql):
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
    testdb = mydb.mydb()
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
            #根据param，分别取到两个接口的广告消耗数据
            for i in range(url_counts):
                result = admin_s.get(str(tmp[i]['url']).format(yestoday, yestoday))
                logger.info('id is ' + str(case[0]))
                logger.info(result.url)
                logger.info(result.text)
                logger.info('expect_value ' + case[3])
                values = result.json()['data']['data']
                if len(values) > 0:
                    re.append((values[0][tmp[i]['cmp_key']])/100)
                else:
                    re.append(0)
            logger.info('汇总报表返回的广告消耗: '+ str(re[0]) + ',' + '广告报表返回的广告消耗是: ' + str(re[1]))
            # id,testcasename,param,expect_value,param_type,`group`
            code_data_tmp = str(case[0]) + '_' + str(case[1]) + '_', case[3], case[4], abs(int(re[0])-int(re[1]))
            cases_data_list.append(code_data_tmp)
        return cases_data_list

if __name__ == '__main__':
    # s=api_admin.adminlogin()
    # adv = api_admin.adv_admin()
    del_gdatas()
    cmp_cases()
