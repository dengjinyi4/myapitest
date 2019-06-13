#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib
import voyager_common as v
serviceurl=v.serviceUrl()
# 站长管理-列表
def masterList_get(s):
    param={'master_account':'123','id':'1','status':'1','company_name':'1','contact_name':'1','contact_phone':'13811501646','create_time':'1'}
    url=serviceurl+'master/masterList.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
# 站长管理-站长删除
def master_del(s):
    param={'ids':'123'}
    url=serviceurl+'master/deleteMaster.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
# 站长管理-获取单个站长信息
def master_get(s):
    param={'id':'123'}
    url=serviceurl+'master/deleteMaster.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
# 站长管理-新增/编辑站长
def master_neworedit(s):
    param={'masterAccount':'123','id':'1','status':'1','company_name':'1','contact_name':'1','contact_phone':'13811501646','create_time':'1'}
    url=serviceurl+'master/masterList.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
# 媒体管理-列表
def mediaList(s):
    param={'id':'123','media_name':'1','status':'1','master_id':'1','master_name':'1','create_time':'13811501646'}
    url=serviceurl+'media/mediaList.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
#媒体管理-获取单个媒体信息
def singlemedia(s):
    param={'id':'123'}
    url=serviceurl+'media/getMedia.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
#媒体管理-删除 
def media_del(s):
    param={'ids':'123'}
    url=serviceurl+'media/deleteMedia.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
#媒体管理-新增/编辑
def media_add(s):
    param={'mediaName':'新传媒','mediaType':'mediaType','masterId':'masterId','masterName':'masterName','coverCrowd':'coverCrowd','adFilterType':'1','adFilterContent':'adFilterContent','adFilterContentIds':'adFilterContentIds'}
    url=serviceurl+'/media/modefiMedia.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
#站长管理-分配媒介经理

def mediaManager(s):
    param={'adverIds':'adverIds','umUserIds':'umUserIds'}
    url=serviceurl+'/media/mediaManager.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
#站长管理-分配关注者
def masterDistriby(s):
    param={'adverIds':'adverIds','umUserIds':'umUserIds'}
    url=serviceurl+'/media/masterDistriby.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#媒体管理-广告位管理-列表
def media_adzonelist(s):   
    param={'adzone_name':'adzone_name','id':'id','status':'status','media_name':'media_name','id':'id','settle_method':'settle_method','actId':'actId','actName':'actName','actStatus':'actStatus','begin_time':'begin_time','end_time':'end_time','create_time':'create_time'}
    url=serviceurl+'/adzone/list.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
   
#媒体管理-广告位管理-获取广告位详情      
def media_getById(s):      
    param={'id':'id'}
    url=serviceurl+'/adzone/getById.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return  


#媒体管理-广告位管理-新增/修改
def media_modefy(s):
    param={'adzoneName':'adzoneName','mediaId':'mediaId','settleMethod':'settleMethod','costPrice':'costPrice','beginTime':'beginTime','endTime':'endTime','adFilterType':'adFilterType','adFilterContent':'adFilterContent','adFilterContentIds':'adFilterContentIds','urlFilter':'urlFilter','urlFilterContent':'urlFilterContent'}
    url=serviceurl+'/adzone/modefy.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#媒体管理-广告位管理-删除
def media_delete(s):
    param={'id':'id'}
    url=serviceurl+'/adzone/delete.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#媒体管理-广告位管理-上线
def media_statusStart(s):
    param={'id':'id'}
    url=serviceurl+'/adzone/statusStart.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 
#媒体管理-广告位管理-下线
def media_statusEnd(s):
    param={'id':'id'}
    url=serviceurl+'/adzone/statusEnd.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#媒体管理-广告位管理-获取关联活动
def media_getLinkAct(s):
    param={'id':'id'}
    url=serviceurl+'/adzone/getLinkAct.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#媒体管理-广告位管理-保存关联活动

def media_saveLinkAct(s):
    param={'adzoneId':'adzoneId','actList':'actList'}
    url=serviceurl+'/adzone/saveLinkAct.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 



      
if __name__ == '__main__':
    # login()
    s=v.login()
    master_get(s)

