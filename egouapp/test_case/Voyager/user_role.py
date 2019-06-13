#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib
import voyager_common as v
serviceurl=v.serviceUrl()
# 修改密码
def updatepassword(s):
    param={'name':'123','pwd':'1','newpwd':'1'}
    url=serviceurl+'login/change_pwd.htm?'
    r=s.get(url,params=param)
    print r.json()['message']
    print r.json()
    return
# 用户管理-列表/用户管理查询()
def userlist(s):
    param={'username':'coldman','descn':'jack','status':'1','create_time':'1'}
    url=serviceurl+'user/ListUser.htm'
    print url
    r=s.get(url,params=param)
    print r.url
    print r.json()
    return
# 用户管理-删除用户按钮()
def userdel(s):
    param={'ids	':'1'}
    url=serviceurl+'user/ListUser.htm'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
# 用户管理-编辑获取单个用户信息()
def useredit(s):
    param={'id	':'1'}
    url=serviceurl+'user/getUser.htm?'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
# 用户管理-编辑/新增用户信息()
def useredit_new(s):
    param={'username':'1','descn':'1','duty':'1','phone':'1','email':'1','alwIds':'1'}
    url=serviceurl+'user/updateUser.htm?'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
# 用户管理-启用/停用 按钮()
def userstart_stop(s):
    param={'status':'1','ids':'1'}
    url=serviceurl+'user/updateStatus.htm?'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
# 角色管理-列表/条件查询()
def user_role_list(s):
    param={'name':'1'}
    url=serviceurl+'role/ListRole.htm?'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
# 角色管理-编辑获取单个角色信息
def user_role_getinforbuyid(s):
    param={'id':'1'}
    url=serviceurl+'role/getRole.htm?'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
# 角色管理-角色信息修改/新增
def user_role_addorupdate(s):
    param={'name':'1','descn':'1','alwIds':'1','id':'1','dataAuth':'1'}
    url=serviceurl+'role/modefiRole.htm?'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
# 角色管理-删除
def user_role_del(s):
    param={'ids':'1'}
    url=serviceurl+'role/deleteRole.htm?'
    print url
    r=s.get(url,params=param)
    print r.json()
    return
def user_role_getMenu(s):  
    url=serviceurl+'role/deleteRole.htm?'
    print url
    r=s.get(url)
    print r.json()
    return




if __name__ == '__main__':
    v.login()