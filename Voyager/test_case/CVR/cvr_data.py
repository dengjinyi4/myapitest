# encoding=utf-8
__author__ = 'aidinghua'

import requests
import json
from utils import db_info
import time,datetime
import random
import string
# import schedule



#获取日期
requests.packages.urllib3.disable_warnings()

class cvr(object):

  def tmpdaylist(self,days):

    d = datetime.datetime.now()

    timedate_from = d+ datetime.timedelta(days=-int(days))

    timedate_from = str(timedate_from)[0:10]

    daylist = timedate_from.replace('-','')

    return daylist

  def timestamp(self):
    # stamp = int(time.time())
    stamp = int(round(time.time()*1000))
    return stamp


  def get_date(self):

    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


  def get_datetime(self):

    return datetime.datetime.now().strftime("%Y%m%d")

  def get_month(self):

    mon = datetime.datetime.now().month

    if  mon<10:
        return "0"+mon
    else:
        return mon





#获取ad_click_tag
  def get_adclicktag(self,ad_choosen_tag):

    sql='''SELECT ad_click_tag FROM voyagerlog.ad_click_log{} WHERE ad_choosen_tag='{}' '''.format(cvr.tmpdaylist(0),ad_choosen_tag)
    time.sleep(3)
    db=db_info.DbOperation(True)
    re=db.excute_sql(sql)
    return re

#调用广告展现接口
  # http://172.16.105.11:17091/ad_bidding.do?pids=1&uniq_tag=11&ip=172.16.144.19&cookie=daf1222111ads&device=IOS&adzone_id=1610&pos_num=1_0&act_id=243
  def ad_show(self,adzoneId):
    param={'pids':1,'uniq_tag':2323211,'ip':'172.16.144.19','cookie':'1sadsd222111','device':'IOS','adzone_id':adzoneId,'pos_num':'1_0','act_id':243}
    param['cookie']=''.join(random.sample(string.ascii_letters+string.hexdigits,20))
    url = "http://172.16.105.11:17091/ad_bidding.do"
    #s=requests.session()
    re=requests.get(url,params=param)
    return re,param['cookie']


#调用广告点击接口

  def ad_click(self,adzoneId):

    re,usercookie=cvr.ad_show(adzoneId)
    # print re.text


    param={'ip':'172.16.144.19','agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1','refer':'https://display.adhudong.com/new/rotary_table_iphonex.html?logId=B3W1CD6H1IJW9MY8RL','adZoneId':adzoneId,'actId':243,'ref':'','mediaId':86,'ctm_code':'Mi8vMTgxNy8vMi8vMi8vODA4NTEvLzE1Mzg5OTA4OTI3ODkvLzZjYWYwZjg4MDliMTQ0OTk2NGQwZDk1NDNhNmY5ZmIyLy9jNTc5NjFhYzZlZjg=','isIntercept':'1','adzone_show_tag':'null','adPlanId':237,'adOrderId':1509,'adCreativeId':1268,'userCookie':'','adLinkUrl':'http://m.baidu.com/','chargeType':2,'advertiserId':2222466,'adChoosenTag':'D3W1CD6R1IJW9NHJ7L','adzoneClickId':'B3W1CD6H1IJW9MY8RL','invalid_message':'','isCharge':1,'logType':2,'status':1,'positionId':1,'occurrence':0,'reach_time':cvr.timestamp(),'award_type':7,'award_type_id':0,'open_id':'null','appid':'','path':'','create_time':cvr.timestamp()}
    param['adOrderId']=re.json()['data']['{"id":1,"positionSize":"640x300","positionType":1,"occurrenceTime":0}'][0]['adOrder']['id']
    param['adCreativeId']=re.json()['data']['{"id":1,"positionSize":"640x300","positionType":1,"occurrenceTime":0}'][0]['adCreative']['id']
    param['advertiserId']=re.json()['data']['{"id":1,"positionSize":"640x300","positionType":1,"occurrenceTime":0}'][0]['adOrder']['advertiserId']
    param['adChoosenTag']=re.json()['data']['{"id":1,"positionSize":"640x300","positionType":1,"occurrenceTime":0}'][0]['tag']
    param['adLinkUrl'] =re.json()['data']['{"id":1,"positionSize":"640x300","positionType":1,"occurrenceTime":0}'][0]['linkUrl']
    param['userCookie']=usercookie
    url="http://172.16.105.11:17091/bridge.do"
    re=requests.get(url,params=param,verify=False)
    print re
    ad_choosen_tag=param['adChoosenTag']
    # print re
    return ad_choosen_tag


#调用效果数据收集接口

  def save_effect(self,adzoneId,count):

    for i in range(0,count):
      param={'ad_click':'','type':'1','uid':'5566','timestamp':''}
      ad_choosen_tag=cvr.ad_click(adzoneId)
      ad_click_tag=cvr.get_adclicktag(ad_choosen_tag)
      param['ad_click']=ad_click_tag
      param['timestamp']=cvr.get_date()
      url="http://open.adhudong.com/saveEffect.htm"

      re = requests.get(url,params=param)
      print ad_click_tag
      print re.text
    return 1



# #数据清除
  def del_data(self,adzoneId):
    sql1 = ''' DELETE FROM  voyagerlog.ad_show_log{} WHERE adzone_id = {}'''.format(cvr.get_datetime(),adzoneId)
    sql2 = ''' DELETE FROM  voyagerlog.ad_click_log{}  WHERE adzone_id ={}'''.format(cvr.get_datetime(),adzoneId)
    sql3 = ''' DELETE FROM  voyagerlog.ad_effect_log_{}  WHERE adzone_id ={} '''.format(cvr.get_month(),adzoneId)
    db=db_info.DbOperation(True)
    time.sleep(2)
    db.delete_sql(sql1)
    time.sleep(2)
    db.delete_sql(sql2)
    time.sleep(2)
    db.delete_sql(sql3)



if  __name__=='__main__':

#单独按广告位调用展现1000次接口
    cvr = cvr()
    # count =0
    # while count<2000:
    #     cvr.ad_show(467)
    # #     cvr.ad_show(1823)
    # #     # cvr.ad_show(1824)
    # #     # cvr.ad_show(1825)
    # #     # cvr.ad_show(1826)
    # #     # cvr.ad_show(1827)
    # #     # cvr.ad_show(1828)
    # #     # cvr.ad_show(1829)
    #     count=count+1
#按照广告位生成990次点击数据

    count=0
    while count<690:
      # cvr.ad_click(1822)
      cvr.ad_show(467)
      # cvr.ad_click(1828)
      # cvr.save_effect(1828, 1)
      time.sleep(10)
      cvr.ad_click(467)
      # cvr.ad_click(1825)
      # cvr.ad_click(1826)
      # cvr.ad_click(1827)
      # cvr.ad_click(1828)
      # cvr.ad_click(1829)
      count=count+1


#按照广告位生成10次效果数据


    # cvr.save_effect(1822,10)
    # cvr.save_effect(1823,10)
    # cvr.save_effect(1824,10)
    # cvr.save_effect(1825,10)
    # cvr.save_effect(1826,10)
    # cvr.save_effect(1827,10)
    # cvr.save_effect(1828,10)
    # cvr.save_effect(1829,20)


#按照广告位删除测试数据
    # del_data(1822)
    # del_data(1823)
    # del_data(1824)
    # del_data(1825)
    # del_data(1826)
    # del_data(1827)
    # del_data(1828)










##单独按广告位调用展现，点击接口
    # count =0
    # while count<1:
    #     ad_click(1822)
    #     count=count+1