# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 16:18
# @Author  : wanglanqing

import requests,json
from test_case.hdtapi_business.test_data.url_data import cookies
from test_case.hdtapi_business.test_data.url_data import *
import sys



def send_request(func_name, url):
    print '===========' + func_name + ' 方法的请求/返回============= '
    print '请求的url是： ', url
    response = requests.get(url, verify=False, cookies =cookies )
    #返回data值
    print '返回的response是： ',  response.text
    try:
        data = response.json()['data']
        print(data)
        return data
    except KeyError as e:
        print '返回的数据中没有data， ', e
        return False
    print 'data : ', data


def send_request_list(func_name, url):
    print '===========' + func_name + ' 方法的请求/返回============= '
    print '请求的url是： ', url
    response = requests.get(url, verify=False, cookies=cookies)
    # 返回data值
    print '返回的response是： ', response.text
    try:
        response = response.json()
        return response
    except KeyError as e:
        print '返回的数据中没有data， ', e
        return False
    print 'data : ', response


def send_request_message(func_name, url):
    print '===========' + func_name + ' 方法的请求/返回============= '
    print '请求的url是： ', url
    response = requests.get(url, verify=False, cookies =cookies )
    #返回data值
    print '返回的response是： ',  response.text
    try:
        msg = response.json()['message']
        return msg
    except Exception as e:
        print '返回的数据中没有message， ', e
        return False
    print 'message : ', msg


def re_err_message(key):
    '''
    缺少参数，或参数不正确时，返回的为message信息，该方法为公用方法
    :param key:url_data中定义的key
    :return:
    '''
    url = url_data[key][0]
    func_name = sys._getframe().f_code.co_name
    response = send_request_message(func_name, url)
    return response

def re_200_data(key):
    '''
    参数请求成功时，返回200信息，返回data数据
    :param key:
    :return:
    '''
    url = url_data[key][0]
    func_name = sys._getframe().f_code.co_name
    response = send_request(func_name, url)
    return response
