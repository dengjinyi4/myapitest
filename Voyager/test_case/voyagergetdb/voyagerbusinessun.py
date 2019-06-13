#encoding: utf-8

import unittest
import checkvoyagerdb as cv

class mycheck(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头 生产环境后台报表api
    def test_hbhk(self):
        '''检查advertiser_balance_log 表中 5：预扣款划拨 6：预扣款回款 金额是否相等 '''
        vaule,tmpstr=cv.getykhb()
        print tmpstr
        self.assertTrue(vaule)
if __name__ =='__main__':
    unittest.main()

