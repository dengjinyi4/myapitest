#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver

import unittest
import yiqifahoutai as y

class mytest(unittest.TestCase):
    
    ##初始化工作
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testcpsbaobiao254(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (listcpshuizong,listcpsmingxi)=y.yqfcpsordershishihuizong(254)
        self.assertTrue(listcpshuizong[0]==listcpsmingxi[0] and listcpshuizong[1]==listcpsmingxi[1] and listcpshuizong[2]==listcpsmingxi[2] and listcpshuizong[3]==listcpsmingxi[3] and listcpshuizong[4]==listcpsmingxi[4] and listcpshuizong[5]==listcpsmingxi[5] and listcpshuizong[6]==listcpsmingxi[6] )
    def testcpsbaobiao17222(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (listcpshuizong,listcpsmingxi)=y.yqfcpsordershishihuizong(17222)
        self.assertTrue(listcpshuizong[0]==listcpsmingxi[0] and listcpshuizong[1]==listcpsmingxi[1] and listcpshuizong[2]==listcpsmingxi[2] and listcpshuizong[3]==listcpsmingxi[3] and listcpshuizong[4]==listcpsmingxi[4] and listcpshuizong[5]==listcpsmingxi[5] and listcpshuizong[6]==listcpsmingxi[6] )
    def testcpsbaobiao18318(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (listcpshuizong,listcpsmingxi)=y.yqfcpsordershishihuizong(18318)
        self.assertTrue(listcpshuizong[0]==listcpsmingxi[0] and listcpshuizong[1]==listcpsmingxi[1] and listcpshuizong[2]==listcpsmingxi[2] and listcpshuizong[3]==listcpsmingxi[3] and listcpshuizong[4]==listcpsmingxi[4] and listcpshuizong[5]==listcpsmingxi[5] and listcpshuizong[6]==listcpsmingxi[6] )
    def testcpsbaobiao139(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (listcpshuizong,listcpsmingxi)=y.yqfcpsordershishihuizong(139)
        self.assertTrue(listcpshuizong[0]==listcpsmingxi[0] and listcpshuizong[1]==listcpsmingxi[1] and listcpshuizong[2]==listcpsmingxi[2] and listcpshuizong[3]==listcpsmingxi[3] and listcpshuizong[4]==listcpsmingxi[4] and listcpshuizong[5]==listcpsmingxi[5] and listcpshuizong[6]==listcpsmingxi[6] )
    def testcpsbaobiao6489(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (listcpshuizong,listcpsmingxi)=y.yqfcpsordershishihuizong(6489)
        self.assertTrue(listcpshuizong[0]==listcpsmingxi[0] and listcpshuizong[1]==listcpsmingxi[1] and listcpshuizong[2]==listcpsmingxi[2] and listcpshuizong[3]==listcpsmingxi[3] and listcpshuizong[4]==listcpsmingxi[4] and listcpshuizong[5]==listcpsmingxi[5] and listcpshuizong[6]==listcpsmingxi[6] )
    def testcpsbaobiao17971(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (listcpshuizong,listcpsmingxi)=y.yqfcpsordershishihuizong(17971)
        self.assertTrue(listcpshuizong[0]==listcpsmingxi[0] and listcpshuizong[1]==listcpsmingxi[1] and listcpshuizong[2]==listcpsmingxi[2] and listcpshuizong[3]==listcpsmingxi[3] and listcpshuizong[4]==listcpsmingxi[4] and listcpshuizong[5]==listcpsmingxi[5] and listcpshuizong[6]==listcpsmingxi[6] )
    def testcpsbaobiao247(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (listcpshuizong,listcpsmingxi)=y.yqfcpsordershishihuizong(247)
        self.assertTrue(listcpshuizong[0]==listcpsmingxi[0] and listcpshuizong[1]==listcpsmingxi[1] and listcpshuizong[2]==listcpsmingxi[2] and listcpshuizong[3]==listcpsmingxi[3] and listcpshuizong[4]==listcpsmingxi[4] and listcpshuizong[5]==listcpsmingxi[5] and listcpshuizong[6]==listcpsmingxi[6] )
if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()