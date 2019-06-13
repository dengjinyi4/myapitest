#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver
import os
import time
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['app']=PATH(r'D:\work\auto\sc\app-auto.apk')
        # desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['deviceName'] = '81GEBN3222JX'
        desired_caps['appPackage'] = 'com.emar.egou'
        desired_caps['appActivity'] = 'com.egou.activity.SplashActivity'
        # desired_caps['appActivity'] = 'com.egou.activity.activity.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon2").is_displayed())
        # 进入商城返利
        self.driver.find_element_by_id('com.emar.egou:id/ad_icon2').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/rrtab_right").is_displayed())
        pass
    
    #退出清理工作
    def tearDown(self):
        self.driver.quit()
        pass
    '''获取屏幕xy值'''
    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return (x, y)
    '''滑动'''
    def swipeUp(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)    #x坐标
        y1 = int(l[1] * 0.75)   #起始y坐标
        y2 = int(l[1] * 0.05)   #终点y坐标
        self.driver.swipe(x1, y1, x1, y2,t)
    def shangchengjump(self,strfanli,strexecpt):
        self.driver.find_element_by_name(strfanli).click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/h_top_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/h_top_title').text
        print strtitle+'\n'
        time.sleep(5)
        egouview=self.driver.find_element_by_id('com.emar.egou:id/e_webview')
        print '页面是否显示 %s'%egouview
        self.assertEqual(strtitle,strexecpt)
    #   点击各个电商，进入电商的详情页
    def shangchengjumpok(self,strfanli,strexecpt,strname):
        self.driver.find_element_by_name(strfanli).click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/h_top_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/h_top_title').text
        print strtitle+'\n'
        time.sleep(5)
        self.assertEqual(strtitle,strexecpt)
        self.assertTrue(self.driver.find_element_by_name(strname).is_displayed())
    #具体的测试用例，一定要以test开头
    def testegouapp_shangcheng_jingdong1(self):
        self.shangchengjumpok('返利可达5.6%',u'京东商城','分类查询')
    # def testegouapp_shangcheng_yougou(self):
    #     self.shangchengjumpok('返利可达7%',u'优购时尚商城','超级秒杀')
    def testegouapp_shangcheng_guomei(self):
        self.shangchengjumpok('返利可达14%',u'国美在线','分类')
    # def testegouapp_shangcheng_dagndang(self):
    #     self.shangchengjumpok('返利可达4.2%',u'当当','图书榜')
    def testegouapp_shangcheng_leshi(self):
        self.shangchengjumpok('返利可达2%',u'乐视商城','全部分类')
    def testegouapp_shangcheng_tianmao(self):
        self.shangchengjumpok('返利可达36%',u'天猫超市','母婴玩具')
    def testegouapp_shangcheng_suningyigou(self):
        self.shangchengjumpok('返利可达2.8%',u'苏宁易购','分类')
    def testegouapp_shangcheng_amazon(self):
        self.shangchengjumpok('返利可达6%',u'亚马逊（卓越网）','海外购')
    def testegouapp_shangcheng_huawei(self):
        self.shangchengjumpok('返利可达3.5%',u'华为商城','以旧换新')
if __name__ =='__main__':

    unittest.main()
	# testunit = unittest.TestSuite()