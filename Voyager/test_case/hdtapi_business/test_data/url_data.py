# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 16:17
# @Author  : wanglanqing

host = 'apidisplay.adhudong.com'
app_key = 'adhu59f6707b8a7147f7'
sign = '74e07c87992bea5f886c7c76131a64fa'
act_id = '59'
adzoneId = '109'
award_get_id = ''
choosen_tag = ''
mediaId = '40'
gather_act_id = '31'
phone = '13621348140'
sign_ad_id = '32'
fall_ad_id = '53'
fall_adzone_id= '398'



#url_data 字典结构说明 ： 接口名:[请求的url, [预期返回的字段list],[预期返回的二级字段的list]，[预期返回的二级字段的list]... , [预期返回的数据] ]
url_data={
    #广告位点击接口
    #"http://apidisplay.adhudong.com/site_login_ijf.htm?app_key=adhu59f6707b8a7147f7&user_id=not_login&sign=74e07c87992bea5f886c7c76131a64fa"
    'site_login' : ["http://{0}/site_login_ijf.htm?app_key={1}&user_id=not_login&sign={2}".format(host, app_key, sign),
                    ['classifi' ,'actId', 'logId', 'adzoneId' ,'mediaId','locationAdress','token','mediaInfo'],
                    [1, 1, "B3W1CD6H1HMW3WFAPT", 109, 40, "https://apidisplay.adhudong.com/spread/rotary-table.htm", "d3744029-a02e-476a-aabb-d87ba6d67ed7"]],

    #中奖公告接口
    'notice_list' : ["http://{0}/notice/list.htm?adzoneId={1}&act_id={2}".format(host, adzoneId, act_id),
                     [],
                     '\d{3}\*{2}\d{4}'],

    #活动推荐接口
    'recommended' : ["http://{0}/activity/recommended.htm?adzone_id={1}&act_id={2}".format(host, adzoneId, act_id),
                     [],
                     ],

    #活动详情接口
    # http://apidisplay.adhudong.com/activity/163.htm?adzoneId=101&logId=B3W1CD6H1HJXPHGC01
    'activity' : ["http://{0}/activity/{1}.htm?adzoneId={2}&logId=".format(host, act_id, adzoneId),
                  ['free_num','css','hours','act','posiList','awards','logId','redPack','adzone','login_type','ads','total_num','mediaInfo'],
                  []],

    #活动信息获取接口获取模板信息
    #http://apidisplay.adhudong.com/preload/activity/59.htm?adzoneId=101&logId=B3W1CD6H1HM5PG9QWX
    'preload_activity' : ["http://{0}/preload/activity/{1}.htm?adzoneId={2}&logId=".format(host, act_id, adzoneId),
                            ['classifi','actId','logId','adzoneId','mediaId','locationsAdress'],
                            []],

    #刷新活动页面接口(剩余次数)
    #http://apidisplay.adhudong.com/user_lottery_info.htm?act_id=163&adzoneId=101&timeSign=1510811182682
    'user_lottery_info' : ["http://{0}/user_lottery_info.htm?act_id={1}&adzoneId={2}&timeSign=".format(host, act_id, adzoneId),
                           ['lottery_left_times'],
                           []],

    #广告详情接口
    #http://apidisplay.adhudong.com/record/award_detail/C3W1CD6H1HLY1FNJZ5.htm?choosen_tag=D3W1CD6R1HLY1FNJZ5
    'award_detail' : ["http://{0}/record/award_detail/{1}.htm".format(host, award_get_id),
                      ['login_type', 'adzoneId', 'award_get_id', ],
                      []],

    #我的奖品
    #http: // apidisplay.adhudong.com / record / lottery_list.htm?logId = B3W1CD6H1HJ9X99JUP & mediaId = 55
    'lottery_list' : ["http://{0}/record/lottery_list.htm?mediaId={1}&logId=".format(host, mediaId),
                      ['clickLogid', 'awardId', 'orderId', 'clickUrl', 'chooseTag', 'ad', 'quanImgUrl', 'quanTitle'],
                      []],

    #聚合活动详情接口
    #    http://apidisplay.adhudong.com/gatherActivity/31.htm?adzoneId=372&logId=B3W1CD6H1HN3051U01
    'gather_activity' : ["http://{0}/gatherActivity/{1}.htm?adzoneId={2}&logId=".format(host, gather_act_id, adzoneId),
                         ['css', 'hours', 'act', 'phone', 'floors', 'logId', 'goldcoin_num'],
                         []],

    #点击抽奖
    #http://apidisplay.adhudong.com/lottery.htm?act_id=232&adzone_click_id=B3W1CD6H1HNSZU90IP&device=IOS&token=69b0ca82-cec6-45df-b1ce-190cd3c96445
    'lottery' : ["http://{0}/lottery.htm?act_id={1}&device=IOS&adzone_click_id=".format(host, act_id),
          ['act_award_id', 'ad', 'award_type','lottery_left_times','record_id', 'token','award_name','baidu_tag','recommend_act_id','act_entrance'],
          []],

    #广告点击，该接口已废弃
    #http://apidisplay.adhudong.com/award_use/award_get_id.htm?adzone_click_id=372
    'award_get_id' : ["http://apidisplay.adhudong.com/award_use/award_get_id.htm?adzone_click_id=372",
          [],
          []],

    #手机号注册登录接口
    #http://apidisplay.adhudong.com/phone_login_ijf.htm?media_id=40&phone=13621348140&adzone_id=109
    'phone_login_ijf': ["http://{0}/phone_login_ijf.htm?media_id={1}&phone={2}&adzone_id={3}".format(host, mediaId, phone, adzoneId),
                        ['code', 'data'],
                     []],


    #签到接口
    'sign' : ["http://{0}/sign.htm?act_id={1}&adzoneId={2}".format(host, sign_ad_id, adzoneId),
            ['code', 'data'],
            []],

    #换个活动
    #http://apidisplay.adhudong.com/activity/next.htm?app_key=adhu59f6707b8a7147f7&act_id=59
    # 'next' : ["http://{0}/activity/next.htm?act_id={1}&app_key={2}".format(host, act_id, app_key),
    #           ['act_id', 'act_name', 'free_num', 'banner_image_url'],
    #           []],

    #换个活动_判断（）
    #http://apidisplay.adhudong.com/activity/times.htm?act_id=59&adzoneId=101
    # 'times' : ["http://{0}/activity/times.htm?act_id={1}&adzoneId={2}".format(host, act_id, adzoneId),
    #            [int],
    #            []],

    #广告活动形式扩展-夺宝营
    #    https://apidisplay.adhudong.com/node/indianaCamp/234.htm?adzoneId=398&actId=234&logId=B3W1CD6H1HP3JDOXFL&ip=172.16.145.173
    'indianaCamp' : ["http://{0}/node/indianaCamp/{1}.htm?adzoneId={2}&actId={3}&logId=B3W1CD6H1HP3JDOXFL&ip=172.16.145.173".format(host, fall_ad_id,fall_adzone_id ,fall_ad_id),
          [['goldcoin_num', 'css', 'hours', 'act', 'floors', 'phone', 'logId'], 20],
          []],

    #幸运抽奖接口
    #http://apidisplay.adhudong.com/activity/act_more.htm?adzone_id=101&adzone_click_id=B3W1CD6H1HM5PG9QWX
    'act_more' : ["http://{0}/activity/act_more.htm?adzone_id={1}&adzone_click_id=".format(host,adzoneId),
                  ['adzone_id', 'scroll', 'adzone_click_id', 'acts','customAct'],
                  #scroll返回的list
                  ['id', 'actType', 'actName', 'bannerImageUrl', 'freeNum', 'floor_icon', 'floor_title', 'beginTime','endTime', 'actRuleInfo', 'status', 'templateId', 'operator', 'locationAddress', 'expand1', 'expand2','customAct','changeTimes','customActRemark','coverImageUrl','pageTips'],
                  #acts返回的list
                  ['id', 'actType', 'actName', 'bannerImageUrl', 'freeNum','actRuleInfo','status', 'templateId',  'locationAddress', 'expand1', 'operator','changeTimes','customAct' ]
                  ],

    'goldcoin_ex_list' : "http://apidisplay.adhudong.com/goldcoin_ex_list.htm?page_num=10&page_size=22",
    'my_gold_list' : "http://apidisplay.adhudong.com/my_gold_list.htm",

    #天降红包，只返回广告
    #https://display.adhudong.com/site_login_ijf.htm?app_key=adhu2f41358594ac499a&user_id=not_login&sign=bc06fcb53fe01a7eb2a32c580bd32832
    # https://display.adhudong.com/new/api/fallEnvelopes.htm?act_id=234&adzone_click_id=B3W1CD6H1HPRD8VRMP
    'fallEnvelopes' : ["http://display.adhudong.com/new/api/fallEnvelopes.htm?act_id={0}&adzone_click_id=".format( fall_ad_id),
                       #data返回的list
                       ['record_id', 'award_name', 'ad', 'act_award_id', 'award_type','baidu_tag'],
                       #ad返回的list
                       ['adtype', 'ad_brief_introduction','advertiser_id', 'ad_id', 'ad_jumpDirectly', 'choosen_tag', 'ad_url', 'ad_name', 'ad_image_url','baidu_tag'],
                       []],

    'fallEnvelopes_500_act_id' : ["http://display.adhudong.com/new/api/fallEnvelopes.htm?&adzone_click_id=B3W1CD6H1HPRFKALHD",
                           "Required Long parameter 'act_id' is not present"],

    'fallEnvelopes_500_adzone_click_id': ["http://display.adhudong.com/new/api/fallEnvelopes.htm?&act_id=412",
                        "Required String parameter 'adzone_click_id' is not present"],

    'sdk_run_500_app_key':["http://apidisplay.adhudong.com/node/sdk_run.htm",
                        "Required String parameter 'app_key' is not present"],

    'sdk_run_500_ip': ["http://apidisplay.adhudong.com/node/sdk_run.htm?app_key=sde148751sdd",
                            "Required String parameter 'ip' is not present"],

    'sdk_run_303_adzone_is_invalid': ["http://apidisplay.adhudong.com/node/sdk_run.htm?app_key=12154dds&ip=127.02.4.3",
                       u"广告位无效!"],

    'sdk_run_200': ["http://apidisplay.adhudong.com/node/sdk_run.htm?ip=127.02.4.3&app_key={}".format(app_key),
                    [u'clickUrl',u'sdk_key']],

    'adzone_show_500_app_key': ["http://apidisplay.adhudong.com/node/adzone_show.htm",
                            "Required String parameter 'app_key' is not present"],

    'adzone_show_500_ip': ["http://apidisplay.adhudong.com/node/adzone_show.htm?app_key={}".format(app_key),
                                "Required String parameter 'ip' is not present"],


    'adzone_show_303_adzone_is_valid': ["http://apidisplay.adhudong.com/node/adzone_show.htm?app_key=12154dds&ip=127.02.4.3",
                                u"广告位无效!"],

    'adzone_show_200': ["http://apidisplay.adhudong.com/node/adzone_show.htm?app_key={}&ip=127.02.4.3".format(app_key),
                        ['clickUrl','adzone_show_tag']],

    'lotteryMsg_500_lottery_click_id': ["http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm",
                        "Required String parameter 'lottery_click_id' is not present"],

    'lotteryMsg_500_award_id': ["http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm?lottery_click_id=123",
                                        "Required Integer parameter 'award_id' is not present"],

    'lotteryMsg_500_phone': ["http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm?lottery_click_id=123&award_id=1452&adzone_id=122",
                                "Required String parameter 'phone' is not present"],

    'lotteryMsg_500_phone_err_format': [
        "http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm?lottery_click_id=123&award_id=1452&adzone_id=122&phone=1245",
        u"请输入正确的手机号格式"],

    'lotteryMsg_500_phone_err_ck': [
        "http://apidisplay.adhudong.com/node/persistence/lotteryMsg.htm?lottery_click_id=123&award_id=1452&adzone_id=122&phone=13012345678",
        u"您存在作弊行为"],

    #20180319新增1. 点击获取奖品说明()，


}

cookies = {
    # 'UM_distinctid':'160342d84c21e6-0adbdf186dc6ba-6010107f-15f900-160342d84c3ad',
    'adhd_wdata1':'Mi8vODI1Ly8yLy8yLy8zODEzMC8vMTUxMjcwMzg4MzczMy8vNDRkY2Q4NmIzZDM2ZTc5OWViZDUyM2JhMTRjOWJiNDQvL2EyZDhmNWY2MzE2MA%3D%3D'
    # 'hdt_admin':'NzYvL3Rlc3QvL251bGwvLzNlMDA4',
    # 'reportAllFilterIds':'%257B%2522filterIds%2522%253A%2522_eq_1-2-3-4-5-6-7-8-9-10-11-12-13-14-15%2522%252C%2522userId%2522%253A%2522MjExLy93YW5nbGFucWluZy8vbnVsbC8vY2QwZjc0MWY1%2522%257D'
}