# encoding=utf-8
__author__ = 'aidinghua'

import datetime
import time
from utils import  db_info


class cal_cvr(object):

    def __init__(self,adzone_id,ad_order_id,url,advertiser_id):
        self.db=db_info.DbOperation(True)
        self.adzone_id=adzone_id
        self.ad_order_id=ad_order_id
        self.url=url
        self.advertiser_id= advertiser_id


##输出计算cvr的日期，今天，昨天，前天
    def datetime(self,i):

        today=datetime.datetime.now()
        date=today+datetime.timedelta(days=-int(i))
        date = str(date)[0:10]
        fal_date=date.replace('-','')
        return str(fal_date)
    def datetime2(self,i):

        today=datetime.datetime.now()
        date=today+datetime.timedelta(days=-int(i))
        date = str(date)[0:10]
        return str(date)

###输出当前日期的月份

    def month(self):

        today=datetime.datetime.now()

        month=today.month
        if month >=10:
          return month

        else:
            month = "0"+str(month)
            return month



##输出--广告位  + 广告订单 +创意url的展现数

    def cal_show(self,i):

        sql = ''' SELECT COUNT(1) FROM  voyagerlog.ad_show_log{}  WHERE adzone_id={} AND ad_order_id={} AND url='%{}%' '''.format(self.datetime(i),self.adzone_id,self.ad_order_id,self.url)
        re_show=self.db.excute_sql(sql)
        return int(re_show)



###输出--广告位  + 广告订单 +创意url的效果数

    def cal_effect(self,i):



        sql='''SELECT count(1) FROM  voyagerlog.ad_effect_log_{} WHERE adzone_id={} AND ad_order_id={} AND url like '%{}%' AND create_time>='{} 00:00:00' and create_time<'{} 23:59:59'  '''.format(self.month(),self.adzone_id,self.ad_order_id,self.url,self.datetime2(i),self.datetime2(i))
        re_effect=self.db.excute_sql(sql)
        return re_effect




###输出--广告位  + 广告订单 +创意url的点击数

    def cal_click(self,i):


        sql=''' SELECT count(1) FROM  voyagerlog.ad_click_log{} WHERE adzone_id={} AND ad_order_id={} AND url like '%{}%' '''.format(self.datetime(i),self.adzone_id,self.ad_order_id,self.url)
        re_click=self.db.excute_sql(sql)
        return re_click


###输出--广告位  + 广告订单 +创意url的CVR

    def cal_cvr(self,i):

        # if  cal_cvr.cal_show(self,i)>=0:

          # (self.adzone_id and self.ad_order_id and self.url)  is not None
          for k in range(0,i):
              # print '=========='
              # print self.cal_effect(k)
              # print self.cal_click(k)
              if self.cal_click(k)<>0:


                  cvr_value= float(self.cal_effect(k))/self.cal_click(k)

                  if k == 0:
                      e=0.5
                  elif k==1:
                      e=0.25
                  elif k==2:
                      e=0.25
                  else:
                      e=0

                  print self.datetime(k),"的cvr值为:",cvr_value,"加权cvr值为:",cvr_value*e






if __name__=='__main__':

    cal = cal_cvr(1822,1635,'https://display.adhudong.com/new/ad/vipjr.html?utm_click=',2361)
    # cal = cal_cvr(1823,1636,'https://display.adhudong.com/new/ad/vipjr.html?utm_click=',2222231)
    # cal = cal_cvr(1824,1637,'https://display.adhudong.com/new/ad/vipjr.html?utm_click=',2222234)
    # cal = cal_cvr(1825,1579,'https://display.adhudong.com/new/ad/vipjr.html?utm_click=',2222238)
    # cal = cal_cvr(1826,1578,'https://display.adhudong.com/new/ad/vipjr.html?utm_click=',2222247)
    # cal = cal_cvr(1827,1639,'https://display.adhudong.com/new/ad/vipjr.html?utm_click=',2222502)
    # cal = cal_cvr(1828,1638,'https://display.adhudong.com/new/ad/vipjr.html?utm_click=',2222263)
    # cal = cal_cvr(1829,1641,'https://ypg.adhudong.com/private/crm/info.html?channel=adhudong&utm_click=',2222558)



print cal.cal_cvr(3)


