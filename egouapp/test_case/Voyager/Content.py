#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib
import voyager_common as v
serviceurl=v.serviceUrl()

#内容管理-模板管理-模板列表
def Content_template_list(s):
    param={'template_name':'template_name','id':'id','template_type_id':'template_type_id','create_time':'create_time','name':'name','update_time':'update_time'}
    url=serviceurl+'/template/list.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#内容管理-模板管理-模板列表-删除
def Content_template_del(s):
    param={'ids':'ids'}
    url=serviceurl+'/template/delete.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#内容管理-模板管理-模板列表-新增/修改
def Content_template_add(s):
    param={'templateTypeId':'templateTypeId','templateName':'templateName','templateStyleId':'templateStyleId','positionId':'positionId'}
    url=serviceurl+'/template/modefy.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return


#内容管理-模板管理-模板编辑-模板样式新增()
def Content_template_styleInsert(s):
    param={'styleName':'styleName','styleUrl':'styleUrl','imageUrl':'imageUrl'}
    url=serviceurl+'/template/styleInsert.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#内容管理-模板管理-模板编辑-模板类型新增
def Content_template_typeInsert(s):
    param={'name':'name','prizesNum':'prizesNum','preview':'preview'}
    url=serviceurl+'/template/typeInsert.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#内容管理-奖品管理-奖品列表
def Content_awardlist(s):
    param={'award_name':'award_name','id':'id','status':'status','award_type':'award_type','is_exchange':'is_exchange','begin_time':'begin_time','end_time':'end_time'}
    url=serviceurl+'/award/list.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#内容管理-奖品管理-奖品列表-使用详情
def Content_award_actList(s):
    param={'awardId':'awardId','create_time':'create_time','status':'status','long_effective':'long_effective'}
    url=serviceurl+'/award/actList.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return

#内容管理-奖品管理-奖品列表-获取详情
def Content_award_getById(s):
    param={'id':'id'}
    url=serviceurl+'/award/getById.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#内容管理-奖品管理-奖品列表-新增/修改

def Content_award_modefi(s):
    param={'awardType':'awardType','id':'id','awardName':'awardName','briefIntroduction':'briefIntroduction','introduction':'introduction','detailImageUrl':'detailImageUrl','coverImageUrl':'coverImageUrl','costPrice':'costPrice','beginTime':'beginTime','endTime':'endTime','introduction':'introduction','getAddress':'getAddress','jumpMode':'jumpMode','timeType':'timeType','afterTake':'afterTake','takeEffective':'takeEffective'}
    url=serviceurl+'/award/modefi.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 
    
#内容管理-奖品管理-奖品列表-删除
def Content_award_del(s):
    param={'ids':'ids'}
    url=serviceurl+'/award/delete.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#内容管理-活动管理-活动列表
def Content_actlist(s):
    param={'id':'id','act_name':'act_name','status':'status','template_name':'template_name','begin_time':'begin_time','end_time':'end_time','create_time':'create_time'}
    url=serviceurl+'/act/list.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#内容管理-活动管理-活动列表-上线
def Content_act_statusStart(s):
    param={'actId':'actId'}
    url=serviceurl+'/act/statusStart.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#内容管理-活动管理-活动列表-下线
def Content_act_statusEnd(s):    
    param={'actId':'actId'}
    url=serviceurl+'/act/statusEnd.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#内容管理-活动管理-活动列表-获取活动详情
def Content_act_getById(s):    
    param={'actId':'actId'}
    url=serviceurl+'/act/getById.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 

#内容管理-活动管理-活动列表-新增/修改
def Content_act_modefy(s):    
    param={'awardList':'awardList','templateId':'templateId','actName':'actName','freeNum':'freeNum','beginTime':'beginTime','endTime':'endTime','longEffective':'longEffective','status':'status','actRuleInfo':'actRuleInfo'}
    url=serviceurl+'/act/modefy.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return 
