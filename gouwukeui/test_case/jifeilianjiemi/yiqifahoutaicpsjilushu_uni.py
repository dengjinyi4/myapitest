#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver

import unittest
import jifeilianjiemi as jiemi

class mytest(unittest.TestCase):
    
    ##初始化工作
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testjiemi139(self):
        '''对n链进行解密，验证解密后的活动id,站点id，链接id，广告主id平台标识等是否正确。产品'''
        mydriver=jiemi.mywebdriver()
        yqfurl='https://p.yiqifa.com/n?k=UZMWD748rI6H1NW7WmLErI6H2mLErntl1QLF6ltl6E' \
               'BHWNKqrI6H3cLErnDlWE276nb9rIW-&e=123456&t=https://www.yhd.com/product/index.do'
        (campainid,websiteid,linkid,Advertiserid,transactionid,pingtaibiaoshi)=jiemi.jifeilianjiemi(mydriver,yqfurl)
        self.assertEqual(campainid,'139')
        self.assertEqual(websiteid,'871361')
        self.assertEqual(Advertiserid,'151')
        self.assertEqual(pingtaibiaoshi,'b')

if __name__ =='__main__':
    unittest.main()
    #testunit = unittest.TestSuite()