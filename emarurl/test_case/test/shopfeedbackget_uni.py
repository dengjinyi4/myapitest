#!/usr/bin/env python
#encoding: utf-8

import unittest
import add_Test
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头       
    def testshopfeedbackget(self):
    	'''测试testshopfeedbackget 查询京东基本信息'''
        for i in range(1,3,1):
            print i
            self.assertEqual(add_Test.add(i), i)

if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()