#!/usr/bin/env python
#encoding: utf-8

import unittest
import gouwuke_Test
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头       
    def testgetgouwuke001(self):
    	'''判断购物客（海淘）返回数据是否超过1800秒'''
        mytime=gouwuke_Test.getgouwuke_haitao()
        mytime=mytime.split(':')
        self.assertTrue(gouwuke_Test.gouwukecomptime(int(mytime[0]),int(mytime[1]),1800))

if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()