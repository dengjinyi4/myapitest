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
    def testyihaodianlog3(self):
        '''monitor 杭州机房183.131.5.3 验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('183.131.5.3:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
    def testyihaodianlog4(self):
        '''monitor 杭州机房183.131.5.4 验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('183.131.5.4:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
    def testyihaodianlog32(self):
        '''monitor 杭州机房 115.231.106.132验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('115.231.106.132:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
    def testyihaodianlog33(self):
        '''monitor 杭州机房 115.231.106.133验证一号店订单是否跟单 活动139'''
        # yqfurl='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
        url=m.geturl('115.231.106.133:19200',u.yiqfalongurl139())
        yhdorder=m.getyihaodianorder(url)
        self.assertTrue(yhdorder<>"")
if __name__ =='__main__':
    unittest.main()
    #testunit = unittest.TestSuite()