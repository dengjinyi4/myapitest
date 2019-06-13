# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 16:33
# @Author  : wanglanqing

import datetime
import time


def get_current_date():
    return datetime.datetime.now().strftime('%Y%m%d')

def get_current_mili_time():
    return str(int(time.time()*1000))
