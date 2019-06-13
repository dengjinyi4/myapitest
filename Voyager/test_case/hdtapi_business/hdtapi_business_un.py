# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 16:18
# @Author  : wanglanqing
import unittest

from test_case.hdtapi_business.test_data.url_data import *
from test_case.hdtapi_business.utils.url_methods import *
from test_case.hdtapi_business.utils.db_methods import *
from test_case.hdtapi_business.utils.date_methods import *
import time,sys,re


class test_hdt_business(unittest.TestCase):


    def setUp(self):
        self.db = DbOperations()
        defaultencoding = 'utf-8'
        if sys.getdefaultencoding() != defaultencoding:
            reload(sys)
        sys.setdefaultencoding(defaultencoding)



    def tearDown(self):
        self.db.close_db()

    def test_0_site_login_api(self):
        '''广告位点击接口：验证接口返回字段列表、查询adzone_click_log表'''
        func_name = sys._getframe().f_code.co_name
        url = url_data['site_login'][0]
        response = send_request(func_name, url)
        if response != False:
            global ad_click_id
            ad_click_id =  response['logId'].strip()
            q_sql = u"select * from voyagerlog.adzone_click_log" + get_current_date() + " WHERE act_id=1" + " and adzone_id=109" + " and media_id=40" + " and adzone_click_id='"  + ad_click_id+ "'"
            #因为kafaka写库有延迟，在此处sleep10秒
            # time.sleep(80)
            self.assertEqual(len(response), len(url_data['site_login'][1]))
            self.assertItemsEqual(response.keys(), url_data['site_login'][1])
            # self.assertEqual(self.db.len_value(q_sql), 1)
            self.db.close_cursor()


    def test_1_lottery_api(self):
        '''点击抽奖接口：验证返回字段是否正确'''
        global  ad_counter
        ad_counter = 0
        func_name = sys._getframe().f_code.co_name
        url = url_data['lottery'][0] + ad_click_id
        response = send_request(func_name, url)
        if response != False:
            print response
            keys = response.keys()
            for k in keys:
                if k == 'ad':
                    ad_counter += ad_counter
                else:
                    self.assertIn(k, url_data['lottery'][1])

    # @unittest.skip("already passed")
    def test_activity_api(self):
        '''活动详情接口：验证接口返回字段列表'''
        url = url_data['activity'][0] + ad_click_id
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        print(response)
        print(url_data['activity'][2])
        if response != False:
            self.assertItemsEqual(response.keys(), url_data['activity'][1])


    #@unittest.skip("already passed")
    def test_notice_list_api(self):
        '''中奖公告接口：验证返回的中奖条目数；验证条目中的关键字，170**1234获得了'''
        url = url_data['notice_list'][0]
        # func_name = sys._getframe().f_code.co_name
        func_name = self.test_notice_list_api.__name__
        response = send_request(func_name, url)
        if response != False:
            self.assertEqual(len(response), 10)
            # self.assertIn(url_data['notice_list'][2], response[0])
            # if re.match(url_data['notice_list'][2],response[0]):
            self.assertTrue(re.match(url_data['notice_list'][2],response[0]))

    #@unittest.skip("already passed")
    def test_recommended_api(self):
        '''活动推荐接口:验证返回的活动条目数'''
        url = url_data['recommended'][0]
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        if response != False:
            self.assertGreater(len(response), 0)

    #@unittest.skip('passed')
    def test_preload_activity_api(self):
        '''活动信息获取接口获取模板信息接口：验证返回列表条目数；'''
        url = url_data['preload_activity'][0] + ad_click_id
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        if response != False:
            self.assertEqual(len(response), 6)

    # #@unittest.skip('already passed')
    def test_1_user_lottery_info_api(self):
        '''刷新活动页面接口:验证返回列表字段'''
        global left_lottery_times
        url = url_data['user_lottery_info'][0] + get_current_mili_time()
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        left_lottery_times = response.values()
        if response != False:
            self.assertItemsEqual(response.keys(), url_data['user_lottery_info'][1])
            self.assertGreater(response.items(), 0)

    #@unittest.skip('already passed')
    #已与开发确认，该接口不再使用，故此注释掉
    # def test_award_detail_api(self):
    #     '''
    #     广告详情接口:
    #         验证;
    #     '''
    #     url = url_data['award_detail'][0]
    #     print '广告详情接口' + url
    #     response = send_request(url)
    #     print response
    #     # self.assertItemsEqual(response.keys(), url_data['award_detail'][1])
    #     pass

    #@unittest.skip('already passed')
    def test_lottery_list_api(self):
        '''我的奖品接口：验证数据库中的奖品数量与接口返回的奖品数量一致'''
        url = url_data['lottery_list'][0] + ad_click_id
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        q_sql = "select * from voyagerlog.lottery_click_log" + get_current_date() + " WHERE adzone_click_id ='"  + ad_click_id + "'"
        if response != False:
            self.assertEqual(self.db.len_value(q_sql), ad_counter)

    #@unittest.skip('already passed')
    def test_gather_activity_api(self):
        '''聚合活动详情接口:验证接口返回关键字'''
        url = url_data['gather_activity'][0] + ad_click_id
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        if response != False:
            self.assertItemsEqual(response.keys() , url_data['gather_activity'][1])

    def test_phone_1login_ijf_api(self):
        '''手机号注册登录接口,验证接口返回字段'''
        url = url_data['phone_login_ijf'][0]
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        if response != False:
            self.assertEqual(response.keys(), url_data['phone_login_ijf'][1])

    def test_phone_2sign_api(self):
        '''签到接口,验证接口返回字段，需在手机号注册登录接口之后执行'''
        url = url_data['sign'][0]
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        if response !=False:
            self.assertEqual(response.keys(), url_data['sign'][1])

    # 与开发人员王占宇确认，times和next两个接口线上环境未使用，故注释掉 2018/01/03
    # def test_next_api(self):
    #     '''换个活动接口：验证接口返回字段'''
    #     url = url_data['next'][0]
    #     func_name = sys._getframe().f_code.co_name
    #     response = send_request(func_name, url)
    #     if response != False:
    #         # for k in response.keys():
    #         self.assertItemsEqual(response.keys(), url_data['next'][1])
    #
    # def test_times_api(self):
    #     '''换个活动-判断接口：验证接口返回字段'''
    #     url = url_data['times'][0]
    #     func_name = sys._getframe().f_code.co_name
    #     response = send_request(func_name, url)
    #     if response != False:
    #         self.assertLessEqual(response, url_data['times'])

    def test_indianaCamp_api(self):
        '''广告活动形式扩展--夺宝营接口：验证返回的data字段；验证返回的actlist长度'''
        url = url_data['indianaCamp'][0]
        func_name = sys._getframe().f_code.co_name
        response = send_request_list(func_name, url)
        if response != False:
            items = response['data'].keys()
            for k in items:
                self.assertIn(k, url_data['indianaCamp'][1][0])
        self.assertLessEqual(len(response['actList']), url_data['indianaCamp'][1][1])

    def test_act_more_api(self):
        '''幸运抽奖接口 ：1.验证返回的数据结构'''
        url = url_data['act_more'][0] + ad_click_id
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        if response != False:
            items = response.keys()
            for k in items:
                self.assertIn(k , url_data['act_more'][1])

            scroll_items = response['scroll'][0].keys()
            for sk in scroll_items:
                self.assertIn(sk, url_data['act_more'][2] )

            act_items = response['acts'][0].keys()
            for ak in act_items:
                self.assertIn(ak ,url_data['act_more'][3])
    # @unittest.expectedFailure
    def test_fallEnvelopes_api(self):
        '''天降红包接口：1.验证返回的数据结构; 2.验证返回的广告订单状态为投放中'''
        url = url_data['fallEnvelopes'][0] + ad_click_id
        sql = "select a.state from voyager.ad_order a where a.id="
        func_name = sys._getframe().f_code.co_name
        response =  send_request(func_name, url)
        print('==-==-23330-=========222222222')
        print(response)

        print('测试方法是： ' ,__name__)
        if response != False :
            #1.验证返回的数据结构
            items = response.keys()
            for k in items :
                self.assertIn(k, url_data['fallEnvelopes'][1])

            ad_items = response['ad'].keys()
            for ak in ad_items:
                self.assertIn(ak, url_data['fallEnvelopes'][2])
            #2.验证返回的广告订单状态为投放中
            ad_id = str(response['ad']['ad_id'])
            ad_state = self.db.execute_select_sql(sql + ad_id)[0][0]
            self.assertEqual(ad_state, 4)

    def test_fallEnvlopes_500_act_id(self):
        '''天降红包接口：1.验证缺少act_id参数时的错误'''
        url = url_data['fallEnvelopes_500_act_id'][0]
        func_name = sys._getframe().f_code.co_name
        response = send_request_message(func_name, url)
        self.assertEqual(response, url_data['fallEnvelopes_500_act_id'][1])


    def test_fallEnvlopes_500_adzone_click_id(self):
        '''天降红包接口：1.验证缺少adzone_click_id参数时的错误'''
        url = url_data['fallEnvelopes_500_adzone_click_id'][0]
        func_name = sys._getframe().f_code.co_name
        response = send_request_message(func_name, url)
        self.assertEqual(response, url_data['fallEnvelopes_500_adzone_click_id'][1])

    #增加sdk_run接口
    def test_sdk_run_500_app_key(self):
        '''jS-SDK请求图片地址, http://apidisplay.adhudong.com/node/sdk_run.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_sdk_run_500_ip(self):
        '''jS-SDK请求图片地址, http://apidisplay.adhudong.com/node/sdk_run.htm?app_key=123kdjd'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])


    def test_sdk_run_303_adzone_is_invalid(self):
        '''jS-SDK请求图片地址,303, http://apidisplay.adhudong.com/node/sdk_run.htm?app_key=12154dds&ip=127.02.4.3'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_sdk_run_200(self):
        '''jS-SDK请求图片地址,200, http://apidisplay.adhudong.com/node/sdk_run.htm?app_key=adhua0bda663684c4b27&ip=127.02.4.3'''
        key = sys._getframe().f_code.co_name[5:]
        url = url_data[key][0]
        func_name = sys._getframe().f_code.co_name
        response = send_request(func_name, url)
        if response:
            self.assertItemsEqual(response.keys(), url_data[key][1])

    def test_adzone_show_500_app_key(self):
        '''广告位展现接口, http://apidisplay.adhudong.com/node/adzone_show.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_adzone_show_500_app_key(self):
        '''广告位展现接口, http://apidisplay.adhudong.com/node/adzone_show.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_adzone_show_500_ip(self):
        '''广告位展现接口, http://apidisplay.adhudong.com/node/adzone_show.htm?app_key=sde124'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_adzone_show_303_adzone_is_valid(self):
        '''广告位展现接口, http://apidisplay.adhudong.com/node/adzone_show.htm?app_key=sde124&ip=123.10.12.1'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_adzone_show_200(self):
        '''广告位展现接口, http://apidisplay.adhudong.com/node/adzone_show.htm?app_key=adhua0bda663684c4b27&ip=123.10.12.1'''
        key = sys._getframe().f_code.co_name[5:]
        response = re_200_data(key)
        if response:
            self.assertItemsEqual(response.keys(), url_data[key][1])

    def test_lotteryMsg_500_lottery_click_id(self):
        '''奖品中奖信息关联手机号, http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_lotteryMsg_500_award_id(self):
        '''奖品中奖信息关联手机号, http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_lotteryMsg_500_phone(self):
        '''奖品中奖信息关联手机号, http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_lotteryMsg_500_phone_err_format(self):
        '''奖品中奖信息关联手机号, http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])

    def test_lotteryMsg_500_phone_err_ck(self):
        '''奖品中奖信息关联手机号, http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm'''
        key = sys._getframe().f_code.co_name[5:]
        self.assertEqual(re_err_message(key), url_data[key][1])


if __name__ =='__main__':
    unittest.main()