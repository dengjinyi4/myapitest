#!/usr/bin/env python
#encoding: utf-8

import unittest
import hdtapi as h
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testnoticelist(self):
    	'''虚假的中奖信息接口 是否返回200'''
        url='''http://apidisplay.adhudong.com/notice/list.htm?adzoneId=101&act_id=166'''
        vaule=h.allmethod(url)
        print(vaule)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testrecommended(self):
    	'''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=168&adzone_id=101'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testlottery_list(self):
    	'''我的奖品页面是否返回200'''
        url='''http://apidisplay.adhudong.com/record/lottery_list.htm?logId=B3W1CD6H1HJ9X99JUP&mediaId=55'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testlottery(self):
    	'''出广告跳转链接200'''
        url='''http://apidisplay.adhudong.com/lottery.htm?act_id=145&adzone_click_id=B3W1CD6H1I1G70ZF7L&device=IOS'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testactivity(self):
    	'''活动详情接口返回详情200'''
        url='''http://apidisplay.adhudong.com/activity/163.htm?adzoneId=101&logId=B0H3ADC01HLYUDOEXT'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testuser_lottery_info(self):
    	'''刷新活动页面接口接口200'''
        url='''http://apidisplay.adhudong.com/user_lottery_info.htm?act_id=163&adzoneId=101&timeSign=1510811182682'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def test_award_detail(self):
    	'''广告详情页接口200'''
        # url='''http://172.16.105.11:17081/record/award_detail/C3W1CD6H1HLY1FNJZ5.htm?choosen_tag=D3W1CD6R1HLY1FNJZ5'''
        url='''http://apidisplay.adhudong.com/record/award_detail/C3W1CD6H1HLY1FNJZ5.htm?choosen_tag=D3W1CD6R1HLY1FNJZ5'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 303)
    # def test_phone_login_ijf(self):
    # 	'''手机号注册登录接口 提供了用户基本信息查询功能 200'''
    #     # url='''http://172.16.105.11:17081/record/award_detail/C3W1CD6H1HLY1FNJZ5.htm?choosen_tag=D3W1CD6R1HLY1FNJZ5'''
    #     url='''http://apidisplay.adhudong.com/phone_login_ijf.htm?media_id=2&phone=13621348140&adzone_id=101'''
    #     vaule=h.allmethod(url)
    #     print '请求地址是：'+url
    #     self.assertIn(vaule, [200])
    # def test_sign(self):
    # 	'''签到接口200'''
    #     # url='''http://apidisplay.adhudong.com/sign.htm?act_id=32&adzoneId=454'''
    #     url='''https://display.adhudong.com/sign.htm?logId=B3W1CD6H1HVXUBX01T&adzoneId=454&act_id=67&ref=&mediaId=67'''
    #     vaule=h.actmethod(url)
    #     print '请求地址是：'+url
    #     self.assertIn(vaule,[401,200])
    # def test_goldcoin_ex_list(self):
    # 	'''可兑换奖品接口200'''
    #     url='''http://apidisplay.adhudong.com/goldcoin_ex_list.htm?page_num=10&page_size=22'''
    #     vaule=h.actmethod(url)
    #     print '请求地址是：'+url
    #     self.assertIn(vaule,[401,200])
    def test_my_gold_list(self):
    	'''我的金币接口200'''
        url='''http://apidisplay.adhudong.com/my_gold_list.htm'''
        vaule=h.actmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[401,200])
    def test_act_more(self):
    	'''幸运抽奖接口接口200'''
        url='''http://apidisplay.adhudong.com/activity/act_more.htm?adzone_id=101&adzone_click_id=B3W1CD6H1HM5PG9QWX'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[200])

    # 与开发人员王占宇确认，times和next两个接口线上环境未使用，故注释掉 2018/01/03
    # def test_times(self):
    # 	'''换个活动-判断接口200'''
    #     url='''http://apidisplay.adhudong.com/activity/times.htm?act_id=59&adzoneId=101'''
    #     vaule=h.allmethod(url)
    #     print '请求地址是：'+url
    #     self.assertIn(vaule,[200])

    # def test_next(self):
    # 	'''换个活动接口200'''
    #     url='''http://apidisplay.adhudong.com/activity/next.htm?act_id=59&adzoneId=109&app_key=adhu59f6707b8a7147f7'''
    #     vaule=h.allmethod(url)
    #     print '请求地址是：'+url
    #     self.assertIn(vaule,[200])
    def test_activity(self):
    	'''活动信息获取接口获取模板信息接口200'''
        url='''http://apidisplay.adhudong.com/preload/activity/59.htm?adzoneId=101&logId=B3W1CD6H1HM5PG9QWX'''

        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[200])
    # def test_jfb_ex_userinfo(self):
    # 	'''兑换集分宝_用户信息金币兑换集分宝_获取用户信息接口200'''
    #     url='''http://apidisplay.adhudong.com/jfb_ex_userinfo.htm'''
    #     vaule=h.actmethod(url)
    #     print '请求地址是：'+url
    #     self.assertIn(vaule,[200])

    '''
    补充以下接口：
    1.广告位点击；
    2.广告点击；
    3.聚合活动详情；
    4.兑换集分宝_保存支付宝账号；
    5.兑换集分宝_兑换
    6.兑换集分宝_短信发送验证码；
    7.兑换集分宝_获取图片验证码
    '''
    def test_adzone_click(self):
        ''' 广告位点击，接口返回200'''
        url = "http://apidisplay.adhudong.com/site_login_ijf.htm?app_key=adhu59f6707b8a7147f7&user_id=not_login&sign=74e07c87992bea5f886c7c76131a64fa"
        value = h.allmethod(url)
        self.assertIn(value, [200])

    def test_ad_click(self):
        '''奖品点击接口，获取接口返回信息200'''
        url = "http://apidisplay.adhudong.com/award_use/award_get_id.htm?adzone_click_id=C3W1CD6H1I1G7UR3GH&position_id=0"
        value = h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(value, [200])

    def test_juhe_act_detail_info(self):
        "聚合活动详情,请求返回结果为200"
        url ="http://apidisplay.adhudong.com/gatherActivity/31.htm?adzoneId=372&logId=B3W1CD6H1HN3051U01"
        value = h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(value, [200])

    #因为线上无集分宝功能，暂时将集分宝用例注释掉。
    # def test_jfb_ex_add_alipay_account(self):
    #     "兑换集分宝_保存支付宝账号"
    #     url = "http://apidisplay.adhudong.com/jfb_ex_add_alipay_account.htm?alipay_acount=see23@162.com"
    #     value = h.allmethod(url)
    #     print '请求地址是：'+ url
    #     self.assertIn(value, [200])
    #
    # def test_jfb_ex_change(self):
    #     "兑换集分宝_兑换"
    #     url = "http://apidisplay.adhudong.com/jfb_ex.htm?jfb_num=1&identify_code=2323"
    #     value = h.allmethod(url)
    #     print '请求地址是：' + url
    #     self.assertIn(value, [200])
    #
    # def test_jfb_ex_sms(self):
    #     "兑换集分宝_短信发送验证码"
    #     url = "http://apidisplay.adhudong.com/jfb_ex_sms.htm?id=d2405eea40f445a1b93f8344234c4470&img_code=7er3"
    #     value = h.allmethod(url)
    #     print '请求地址是：' + url
    #     self.assertIn(value, [200])
    #
    # def test_jfb_ex_getimgcode(self):
    #     "兑换集分宝_获取图片验证码"
    #     url = "http://apidisplay.adhudong.com/jfb_ex_getimgcode.htm""
    #     value = h.allmethod(url)
    #     print '请求地址是：' + url
    #     self.assertIn(value, [200])

    #增加夺宝营活动的接口
    def test_indianaCamp(self):
        '''广告活动形式拓展--夺宝营'''
        url = "https://apidisplay.adhudong.com/node/indianaCamp/53.htm?adzoneId=398&actId=53&logId=B3W1CD6H1HP3JDOXFL&ip=172.16.145.173"
        value = h.allmethod(url)
        print '请求地址是： ' + url
        self.assertIn(value, [200])


    def test_fallEnvelopes(self):
        '''天降红包，只返回广告'''
        url = "https://display.adhudong.com/new/api/fallEnvelopes.htm?act_id=53&adzone_click_id=B3W1CD6H1I1C67NDQ9"
        value = h.allmethod(url)
        print '请求地址是： ' + url
        self.assertIn(value, [200])


if __name__ =='__main__':
    unittest.main()
