#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib
import voyager_common as v
serviceurl=v.serviceUrl()

# 广告主管理-账号管理列表
def advertiser_account_manage(s):
    param={'id':'123','username':'1','state':'1','type':'1','company':'1','contact_name':'13811501646','contact_phone':'1','create_time':'1'}
    url=serviceurl+'/advertiser/list.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#广告主管理/站长管理--获取分配的经理
def advertiser_getDistriby(s):
    param={'id':'123','username':'1','status':'1','descn':'1'}
    url=serviceurl+'/advertiser/getDistriby.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return


#广告主管理-账号管理 分配关注者

def advertiser_distriby(s):
    param={'adverIds':'adverIds','umUserIds':'umUserIds' }
    url=serviceurl+'/advertiser/distriby.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#广告主管理-跳转到资质审核页
def advertiser_toAptitude(s):
    param={'adverId':'adverId'}
    url=serviceurl+'/advertiser/toAptitude.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
#广告主管理-审核广告主：通过/审核驳回
def advertiser_check_advertiser(s):
    param={'adverId':'adverId','state':'state','reason':'reason','reasoncheck':'reasoncheck'}
    url=serviceurl+'/advertiser/cheque.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#广告主管理-订单管理
def advertiser_orderList(s):
    param={'name':'name','id':'id','plan_id':'plan_id','name':'name','username':'username','advertiser_id':'advertiser_id','state':'state','payment_mode':'payment_mode','contact_phone':'contact_phone','create_time':'create_time'}
    url=serviceurl+'/advertiser/orderList.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
#广告主管理-订单暂停开始
def advertiser_ordersuspend(s):
    param={'orderIds':'orderIds','status':'status'}
    url=serviceurl+'/advertiser/orderSuspend.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#广告主管理-创意列表
def advertiser_creativelist(s):
    param={'id':'id','name':'name','advertiser_id':'advertiser_id','username':'username','state':'state','create_time':'create_time'}
    url=serviceurl+'/advertiser/creativelist.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
    
#广告主管理-查看原因
def advertiser_getReason(s):
    param={'id':'id'}
    url=serviceurl+'/advertiser/getReason.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
 
#广告主管理-跳转创意审核页面
def advertiser_toCreativeReview(s):
    param={'id':'id'}
    url=serviceurl+'/advertiser/toCreativeReview.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return    

#广告主管理-创意管理使用详情
def advertiser_useDetails(s):
    param={'id':'id','state':'state','advertiserId':'advertiserId','adverName':'adverName','orderName':'orderName'}
    url=serviceurl+'/advertiser/useDetails.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return  

#广告主管理-订单详情    
def advertiser_orderDetail(s):
    param={'id':'id','state':'state','advertiserId':'advertiserId','adverName':'adverName','orderName':'orderName'}
    url=serviceurl+'/advertiser/useDetails.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return  

#广告主管理-账号管理查看原因
def advertiser_getAccountReason(s):
    param={'id':'id','status':'status','reasoncheck':'reasoncheck','reason':'reason'}
    url=serviceurl+'/advertiser/getAccountReason.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return  

#广告主管理-创意审核：通过/驳回
def advertiser_creativeReview(s):
    param={'id':'id','status':'status','reasoncheck':'reasoncheck','reason':'reason'}
    url=serviceurl+'/advertiser/getAccountReason.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return  
    
#广告主管理-广告主暂停/启用
def advertiser_suspend(s):
    param={'adverIds':'adverIds','status':'status'}
    url=serviceurl+'/advertiser/suspend.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return   

#广告主管理-账号管理 分配优化师
def advertiser_serviceManager(s):   
    param={'adverIds':'adverIds','umUserIds':'umUserIds'}
    url=serviceurl+'/advertiser/serviceManager.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#广告主管理-账号管理 分配销售经理
def advertiser_salesManager(s):
    param={'adverIds':'adverIds','umUserIds':'umUserIds'}
    url=serviceurl+'/advertiser/serviceManager.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return  