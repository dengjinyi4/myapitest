#!/usr/bin/env python
#encoding: utf-8

import unittest
import fanpai as f
import jiugongge as j
import laohuji as l
import lunpan 
import wawaji as w
import zadan as z
import newlunpan as n
import taoniu as t
import guaguaka as g
import niudan as niu
import iphonexlunpan as iphonex
import shouqianba as s
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def test_fanpai_activity(self):
    	'''翻牌活动是否入了四张表,adzone_id:305,act_id:164'''
        c=f.fanpaicount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_jiugongge_activity(self):
    	'''九宫格活动是否入了四张表,adzone_id:304,act_id:17'''
        c=j.jiugonggecount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_laohuji_activity(self):
        '''老虎机活动是否入了四张表,adzone_id:313,act_id:166'''
        c=l.laohujicount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_lunpan_activity(self):
        '''轮盘活动是否入了四张表,adzone_id:303,act_id:108'''
        c=lunpan.lunpancount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_wawaji_activity(self):
        '''娃娃机活动是否入了四张表,adzone_id:308,act_id:168'''
        c=w.wawajicount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_zadan_activity(self):
        '''砸蛋活动是否入了四张表,adzone_id:307,act_id:115'''
        c=z.zadanwawajicount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_newlunpan_activity(self):
        '''大转盘2.0活动是否入了四张表,adzone_id:310,act_id:165'''
        c=n.newlunpancount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_taoniu_activity(self):
        '''套牛活动是否入了四张表,adzone_id:316,act_id:169'''
        c=t.taoniucount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c),4)
    def test_guaguaka_activity(self):
        '''刮刮卡是否入了四张表,adzone_id:98,act_id:163'''
        c=g.count()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c),4)
    def test_niudan_activity(self):
        '''扭蛋是否入了四张表,adzone_id:401,act_id:196'''
        c=niu.niudancount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c),4)
    def test_iphonexlunpan_activity(self):
        '''iphonex轮盘抽奖是否入了四张表,adzone_id:414,act_id:243'''
        c=iphonex.iphonexlunpancount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c),4)
    def test_shouqianba_activity(self):
        '''收钱吧抽奖是否入了四张表,adzone_id:1597,act_id:333'''
        c=s.shouqianbacount()
        print '四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c),19)
if __name__ =='__main__':
    unittest.main()


	#testunit = unittest.TestSuite()