#!/usr/bin/env python
#encoding: utf-8

import unittest
import chaojifan_test
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头       
    def testproductSearchlendata(self):
    	'''测试高佣api返回的data的个数是否是200'''
        vaule=productSearch_Test.productSearch('150',1)
        data=vaule['data']
        lendata=len(data)
        self.assertEqual(lendata, 1)
    def testproductSearch02(self):
        """测试高佣api返回的data的key值是否和期望的key值相等
        """
        print 'testproductSearch02'
        value=productSearch_Test.productSearch('150',1)
        data=value['data']
        # Expectlist=['productId','productName','pc-productYiqifaUrl','moblie-productYiqifaUrl','pc-discountPrice','moblie-discountPrice','pc-reservePrice','moblie-reservePrice','picUrl','brands','storeName','isPost','volume','volumeOfMonth','Category1Id','Category1Name','Category2Id','Category2Name','startTime','endTime','isRelatedSales','pc-comissionRate','moblie-comissionRate','describe','businessId','businessName','self-support','status']
        Expectlist=['productId','productName','pc-productYiqifaUrl','moblie-productYiqifaUrl','pc-discountPrice','moblie-discountPrice','pc-reservePrice','moblie-reservePrice','picUrl','brands','storeName','isPost','volume','Category1Id','Category1Name','Category2Id','Category2Name','startTime','endTime','isRelatedSales','pc-comissionRate','moblie-comissionRate','describe','businessId','businessName','self-support','status','merchantType']
        Expectlist.sort()
        actlist=data[0].keys()
        actlist.sort()
        print Expectlist
        print actlist
        self.assertListEqual(Expectlist,actlist)
    def testproductserch03(self):
        '''测试高佣api返回的data的key值是否都相同'''
        # print 'testproductserch03'
        value=productSearch_Test.productSearch('150',200)
        data=value['data']
        Explist=data[0].keys()
        Explist.sort()
        # print type(data)
        for actlist in data:
            actlist=actlist.keys()
            actlist.sort()
            self.assertListEqual(Explist,actlist)


if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()