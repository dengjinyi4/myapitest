#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver

import unittest
import monitor_test as m
import yiqifaurl as u

class mytest(unittest.TestCase):
    
    ##初始化工作
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testyihaodianlog77(self):
        '''monitor 亦庄机器123.59.17.77 验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('123.59.17.77:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
    def testyihaodianlog235(self):
        '''monitor 亦庄机器123.59.17.235 验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('123.59.17.235:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
    def testyihaodianlog23(self):
        '''monitor 亦庄机器123.59.111.23验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('123.59.111.23:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
    def testyihaodianlog236(self):
        '''monitor 亦庄机器123.59.17.236验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('123.59.17.236:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
if __name__ =='__main__':
    unittest.main()
    #testunit = unittest.TestSuite()