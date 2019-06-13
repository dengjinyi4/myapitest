#!/usr/bin/env python
#encoding: utf-8

import unittest
import yiqifaProductEnv_Test
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testyiqifahoutaia(self):
    	'''测试后台机器ip： 是否返回200'''
        url='''http://221.122.127.226:19100/mgrLoginForm.do'''
        vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
        self.assertEqual(vaule, '200')
    def test_yiqifahoutaiq(self):
        '''测试后台机器ip： 是否返回200'''
        url='''http://221.122.127.211:19100/mgrLoginForm.do'''
        vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
        self.assertEqual(vaule, '200')
    def testyiqifahoutai193(self):
    	'''测试后台机器ip： 是否返回200'''
        url='''http://221.122.127.193:19100/mgrLoginForm.do'''
        vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
        self.assertEqual(vaule, '200')
    def testyiqifahoutai194(self):
    	'''测试后台机器ip： 是否返回200'''
        url='''http://221.122.127.194:19100/mgrLoginForm.do'''
        vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
        self.assertEqual(vaule, '200')

    def testyiqifahoutai226s(self):
    	'''测试后台机器ip： 是否返回200'''
        url='''https://221.122.127.226:19103/mgrLoginForm.do'''
        vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
        self.assertEqual(vaule, '200')
    # def testyiqifahoutai211s(self):
    # 	'''测试后台机器ip： 是否返回200'''
    #     url='''https://221.122.127.211:19103/mgrLoginForm.do'''
    #     vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
    #     self.assertEqual(vaule, '200')
    # def testyiqifahoutai193s(self):
    # 	'''测试后台机器ip： 是否返回200'''
    #     url='''https://221.122.127.193:19103/mgrLoginForm.do'''
    #     vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
    #     self.assertEqual(vaule, '200')
    # def testyiqifahoutai194s(self):
    # 	'''测试后台机器ip： 是否返回200'''
    #     url='''https://221.122.127.194:19103/mgrLoginForm.do'''
    #     vaule=yiqifaProductEnv_Test.yiqifaProductEnv(url,'status')
    #     self.assertEqual(vaule, '200')
if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()