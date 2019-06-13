#!/usr/bin/env python
#encoding: utf-8
import unittest

from test_case.hdtapi import hdtapi


class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass

    #退出清理工作
    def tearDown(self):
        pass

    #具体的测试用例，一定要以test开头
    def testbidding85(self):
    	'''验证单台机器上123.59.17.85:17200模拟投放广告接口是否返回广告'''
        print 'test'
        count= hdtapi.ad_simulation('123.59.17.85:17200')
        # 广告个数
        print count
        self.assertTrue(count>0)

if __name__ =='__main__':

    unittest.main()
	#testunit = unittest.TestSuite()