#!/usr/bin/env python
#encoding: utf-8

import unittest
import emargeturl_Test
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头       
    def testgetjdcampaign001(self):
    	'''判断京东商城活动通过p.egou.com出去以后的网站主id是否是65742 亿起发联盟id：17222'''
        jdurl=r'http://p.egou.com/n?k=2mLErnWFWlwLrI6H2mLErI6HWNRSWE4H6EKm6n4H6EDmrZU61BAgpmqerI6H353L6n3F15BH2L--&e=%user%&t=http://www.jd.com/'
        vaule=emargeturl_Test.getjdurl(jdurl)
        self.assertEqual(int(vaule), 65742)
    def testgetjdproduct002(self):
    	'''判断京东商城商品通过p.egou.com出去以后的网站主id是否是65742 亿起发联盟id：17222'''
        jdurl=r'http://p.egou.com/n?k=2mLErnWFWlwLrI6H2mLErI6HWNRSWE4H6EKm6n4H6EDmrZU61BAgpmqerI6H353L6n3F15BH2L--&e=%user%&t=%url%'
        vaule=emargeturl_Test.getjdurl(jdurl)
        self.assertEqual(int(vaule), 65742)
    def testgetjd360buycampaign003(self):
    	'''判断京东商城（360buy） 活动通过p.yiqifa.com出去以后的网站主id是否是150 亿起发联盟id：254'''
        jdurl=r'http://p.yiqifa.com/c?s=c5bdd5a5&w=150&c=254&i=160&l=0&e=%user%&t=http://www.jd.com'
        vaule=emargeturl_Test.getjd360buyurl(jdurl)
        self.assertEqual(int(vaule), 150)
    def testgetjd360buyproduct004(self):
    	'''判断京东商城（360buy）商品通过p.yiqifa.com出去以后的网站主id是否是150 亿起发联盟id：254'''
        jdurl=r'http://p.yiqifa.com/c?s=c5bdd5a5&w=150&c=254&i=160&l=0&e=%user%&t=%url%'
        vaule=emargeturl_Test.getjd360buyurl(jdurl)
        self.assertEqual(int(vaule), 150)
    def testgetjdmobilecampaign005(self):
    	'''判断京东商城（京东商城（移动））商品通过p.egou.com出去以后的网站主id是否是150 亿起发联盟id：17994'''
        jdurl=r'http://p.egou.com/n?k=2mLErnDS6N3erI6H2mLErI6HWNRe1NgH6lDLWntqrn376mLErZyH2mq8WlX91njLMZqbknb_Wy6H&e=%user%&t=http://m.jd.com'
        vaule=emargeturl_Test.getjdurl(jdurl)
        self.assertEqual(int(vaule), 740011)
    def testgetjdmobileproduct(self):
    	'''判断京东商城（京东商城（移动））商品通过p.egou.com出去以后的网站主id是否是150 亿起发联盟id：17994'''
        jdurl=r'http://p.egou.com/n?k=2mLErnDS6N3erI6H2mLErI6HWNRe1NgH6lDLWntqrn376mLErZyH2mq8WlX91njLMZqbknb_Wy6H&e=%user%&t=%url%'
        vaule=emargeturl_Test.getjdurl(jdurl)
        self.assertEqual(int(vaule), 740011)
if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()