#!/usr/bin/env python
#encoding: utf-8

import unittest
import api_admin as h
from parameterized import parameterized
from test_case.voyager_apiadmin import hdtapi

class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):

        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头 生产环境后台报表api
    def testtotalDetail(self):
        '''汇总报表接口 是否返回200'''
        vaule=h.totalDetail()
        print '汇总报表返回状态码不是200'
        self.assertEqual(vaule, 200)
    def testreportZone(self):
        '''媒体报表接口 是否返回200'''
        vaule=h.reportZone()
        print '媒体报表返回状态码不是200'
        self.assertEqual(vaule, 200)
    def testreportOrder(self):
        '''广告报表接口 是否返回200'''
        vaule=h.reportOrder()
        print '广告报表返回状态码不是200'
        self.assertEqual(vaule, 200)
    def testreportDay(self):
        '''经营分析报表接口 是否返回200'''
        vaule=h.reportOrder()
        print '经营分析报报表返回状态码不是200'
        self.assertEqual(vaule, 200)

class adreport(unittest.TestCase):
    @parameterized.expand(hdtapi.cmp_cases(7))
    def test_cmp_cases(self, casename, expected, param_type, Actual, apiname, re, re_url):
        print '用例名称:{}\n'.format(apiname)
        print '请求地址:{}\n'.format(re_url)
        print '请求结果:{}\n'.format(re)
        print '其差值为: {} (金额数据，单位为分)\n'.format(str(Actual))
        self.assertLessEqual(int(Actual), int(expected))

if __name__ =='__main__':
    unittest.main()


	#testunit = unittest.TestSuite()