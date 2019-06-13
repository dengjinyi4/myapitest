# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 9:22
# @Author  : wanglanqing

import logging
import time


class CommonLog(logging.Logger):
    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.INFO)
        now = time.strftime('%Y%m%d%H%M%S')
        # log_formatter = logging.Formatter("[%(levelname)s] %(asctime)s [%(module)s] at line %(lineno)d , func is %(funName)s():] %(message)s,%(message)s,%(message)s ")
        log_formatter = logging.Formatter("[%(levelname)s] %(asctime)s [%(module)s] at line %(lineno)d ]: %(message)s ")
        # log_formatter = logging.Formatter(" %(message)s ")
        filehandler = logging.FileHandler('hdt_api' + now + '.log')
        filehandler.setFormatter(log_formatter)
        self.addHandler(filehandler)
        return