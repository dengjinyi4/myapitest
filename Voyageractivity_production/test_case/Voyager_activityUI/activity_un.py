#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append('../..')
import Emar_SendMail_Attachments as myemail
import unittest,time,json
import requests as r
import fanpai as f
import jiugongge as j
import laohuji as l
import lunpan 
import wawaji as w
import zadan as z
import hdtapi as h

class mytest85(unittest.TestCase):    
    #初始化工作
    @classmethod
    def setUpClass(self):
        print '123.59.17.85测试开始'
        myemail.myini('123.59.17.85','106')
        # try:
        #     re=r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.16&destip=123.59.17.106')
        #     print re.text
        #     if (re.json()['code']==200):
        #         pass
        #     else:
        #         print '调用接口返回值不是200'
        #         myemail.senderrormail(['dengjinyi@emar.com'],'自动化测试出现异常1','环境初始化脚本出现异常请检查'+str(re.text))
        #         raise NameError('环境初始化脚本出现异常请检查')
        # except Exception, e:
        #     myemail.senderrormail(['dengjinyi@emar.com'],'自动化测试出现异常','环境初始化脚本出现异常请检查 调用方法http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.16&destip=123.59.17.106 出现异常 ')
        #     raise NameError('环境初始化脚本出现异常请检查')        
        time.sleep(6)
        pass

    #退出清理工作
    @classmethod
    def tearDownClass(self):
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=123.59.17.106')
        print '123.59.17.85测试结束,nginx重置成123.59.17.106'
        myemail.myini('123.59.17.106','106')
        time.sleep(6)
        pass

    #具体的测试用例，一定要以test开头
    def test_fanpai_activity85(self):
    	'''生产环境(123.59.17.85)翻牌活动是否入了四张表'''
        c=f.fanpaicount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_lunpan_activity85(self):
        '''生产环境(123.59.17.85)轮盘活动是否入了四张表'''
        c=lunpan.lunpancount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def testapirecommended85(self):
        '''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=21&adzone_id=270'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)

class mytest11(unittest.TestCase):    
    #初始化工作
    @classmethod
    def setUpClass(self):
        # print '123.59.17.11测试开始'

        # myemail.myini('123.59.17.11','106')

        # try:
        #     re=r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.16&destip=123.59.17.106')
        #     print re.text
        #     if (re.json()['code']==200):
        #         pass
        #     else:
        #         print '调用接口返回值不是200'
        #         myemail.senderrormail(['dengjinyi@emar.com'],'自动化测试出现异常1','环境初始化脚本出现异常请检查'+str(re.text))
        #         raise NameError('环境初始化脚本出现异常请检查')
        # except Exception, e:
        #     myemail.senderrormail(['dengjinyi@emar.com'],'自动化测试出现异常','环境初始化脚本出现异常请检查 调用方法http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.16&destip=123.59.17.106 出现异常 ')
        #     raise NameError('环境初始化脚本出现异常请检查')        
        time.sleep(6)
        pass

    #退出清理工作
    @classmethod
    def tearDownClass(self):
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=123.59.17.106')
        # print '123.59.17.11测试结束,nginx重置成123.59.17.106'

        # myemail.myini('123.59.17.106','106')
        
        # time.sleep(6)
        pass

    #具体的测试用例，一定要以test开头
    def test_fanpai_activity11(self):
        '''生产环境(123.59.17.11)翻牌活动是否入了四张表'''
        c,logid=f.fanpaicount()
        print '生产环境活动报错,adzonid:%s'%logid
        # print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_lunpan_activity11(self):
        '''生产环境(123.59.17.11)轮盘活动是否入了四张表'''
        c,logid=lunpan.lunpancount()
        # print '生产环境四张表内返回的数据个数是：'+str(c)
        print '生产环境活动报错,adzonid:%s'%logid
        self.assertEqual(int(c), 4)
    def testapirecommended11(self):
        '''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=21&adzone_id=270'''
        vaule=h.allmethod(url)
        # print '请求地址是：'+url
        self.assertEqual(vaule, 200)

class mytest120(unittest.TestCase):    
    ##初始化工作
    @classmethod
    def setUpClass(self):
        print '123.59.17.120测试开始'
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=123.59.17.120')
        myemail.myini('123.59.17.120','106')
        time.sleep(6)
        pass
    #退出清理工作
    @classmethod
    def tearDownClass(self):
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=123.59.17.106')
        myemail.myini('123.59.17.120','106')
        time.sleep(6)
        print '123.59.17.120测试结束,nginx重置成123.59.17.106'
        pass

    #具体的测试用例，一定要以test开头
    def test_fanpai_activity120(self):
        '''生产环境(123.59.17.120)翻牌活动是否入了四张表'''
        c=f.fanpaicount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_lunpan_activity120(self):
        '''生产环境(123.59.17.120)轮盘活动是否入了四张表'''
        c=lunpan.lunpancount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def testapirecommended120(self):
        '''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=21&adzone_id=270'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)

class mytest127(unittest.TestCase):    
    ##初始化工作
    @classmethod
    def setUpClass(self):
        print '221.122.127.127测试开始'
        myemail.myini('221.122.127.127','106')
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=221.122.127.127')
        time.sleep(6)
        pass
    #退出清理工作
    @classmethod
    def tearDownClass(self):
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=123.59.17.106')
        myemail.myini('123.59.17.106','106')
        time.sleep(6)
        print '221.122.127.127测试结束,nginx重置成123.59.17.106'
        pass

    #具体的测试用例，一定要以test开头
    def test_fanpai_activity127(self):
        '''生产环境(221.122.127.127)翻牌活动是否入了四张表'''
        c=f.fanpaicount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_lunpan_activity85(self):
        '''生产环境(123.59.17.127)轮盘活动是否入了四张表'''
        c=lunpan.lunpancount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def testapirecommended127(self):
        '''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=21&adzone_id=270'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)

class mytest131(unittest.TestCase):    
    ##初始化工作
    @classmethod
    def setUpClass(self):
        print '221.122.127.131测试开始'
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=221.122.127.131')
        myemail.myini('221.122.127.131','106')
        time.sleep(6)
        pass
    #退出清理工作
    @classmethod
    def tearDownClass(self):
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=123.59.17.106')
        myemail.myini('123.59.17.106','106')
        time.sleep(6)
        print '221.122.127.131测试结束,nginx重置成123.59.17.106'
        pass

    #具体的测试用例，一定要以test开头
    def test_fanpai_activity131(self):
        '''生产环境(221.122.127.131)翻牌活动是否入了四张表'''
        c=f.fanpaicount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_lunpan_activity131(self):
        '''生产环境(123.59.17.131)轮盘活动是否入了四张表'''
        c=lunpan.lunpancount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def testapirecommended131(self):
        '''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=21&adzone_id=270'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)

class mytest157(unittest.TestCase):    
    ##初始化工作
    @classmethod
    def setUpClass(self):
        print '221.122.127.157测试开始'
        myemail.myini('221.122.127.157','106')
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=221.122.127.157')
        time.sleep(6)
        pass
    #退出清理工作
    @classmethod
    def tearDownClass(self):
        myemail.myini('123.59.17.106','106')
        # r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip=123.59.17.106')
        time.sleep(6)
        print '221.122.127.157测试结束,nginx重置成123.59.17.106'
        pass

    #具体的测试用例，一定要以test开头
    def test_fanpai_activity157(self):
        '''生产环境(221.122.127.157)翻牌活动是否入了四张表'''
        c=f.fanpaicount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def test_lunpan_activity157(self):
        '''生产环境(123.59.17.157)轮盘活动是否入了四张表'''
        c=lunpan.lunpancount()
        print '生产环境四张表内返回的数据个数是：'+str(c)
        self.assertEqual(int(c), 4)
    def testapirecommended157(self):
        '''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=21&adzone_id=270'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)        

if __name__ =='__main__':
    unittest.main()


	#testunit = unittest.TestSuite()