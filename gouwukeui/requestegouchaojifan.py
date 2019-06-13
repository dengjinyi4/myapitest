#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,ssl
def get_taobaourl(url):
    # get t_js url
    refer=requests.get(url,timeout=6).url
    print refer
    headers={'Referer':refer}
    # get taobaourl
    taobaourl=requests.get(urllib.unquote(refer.split('tu=')[1]),headers=headers).url
    # print taobaourl
    # taobaourl=requests.get(urllib.unquote(refer.split('tu=')[1]),headers=headers).url.split('&ali_trackid=')[0]
    return taobaourl.split(':')[2]
    pass
def get_taobaourlu(url):
    r=requests.get(url).url
    print r
    header={'Referer':r}
    # e=requests.get('http://www.baidu.com/s', params={'wd': '4444','rrr':'55555'}).url
    print '----------'
    print 'one is %s'%urllib.unquote(r.split('tu=')[1])
    print '----------'
    e=requests.get(urllib.unquote(r.split('tu=')[1]), headers=header).url
    return e
    pass
def getyiqifaurl(url):
    print '-------入参----------'
    print url
    # print '------p.yiqifa.com l跳------'
    r=requests.get(url,verify=False).url
    # print '1111111111 cmp.emarbox.com 111111111111111'
    # print requests.get(url).text
    # print '-----union.click jdc url----'
    lresponse=requests.get(r,verify=False)
    unionurl=lresponse.text.split('url=')[1].split('"')[0]
    print '++++++++union.click  jda url+++++++'
    print unionurl
    print '++++++++union.click  jda url+++++++'
    # print lresponse.text
    try:
        jdaresponse=requests.get(unionurl)
    except requests.RequestException as e:
        print(e.message)
    jdaurl=jdaresponse.text.split('hrl=\'')[1].split('\'')[0]
    print jdaurl
    try:
        print '----jdresponseurl------'
        # ssl._create_default_https_context = ssl._create_unverified_context
        # jdresponseurl=requests.get(jdaurl,verify=False).url
        context = ssl._create_unverified_context()
        jdresponseurl=requests.get(jdaurl,verify=False).url
        print ('+++++jdresponseurl++++++')
        print jdresponseurl
        print ('+++++jdresponseurl++++++')
    except requests.RequestException as e:
        print('访问union.click.jd.com 报错！')
        print(e)
    return jdresponseurl
    pass
if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    # url=r'http://s.click.taobao.com/t?e=m%3D2%26s%3D6ewufROtMxAcQipKwQzePOeEDrYVVa64K7Vc7tFgwiG3bLqV5UHdqVsgUpKAe02fgL3PGTnk8MYJP4K179EbccpnqzFnZ74a4uco3Q5L6cCh5wPjo7Y%2BcFDyNK%2Bk0VgGwmCco2Dx0scPC4MIsny67Xv4zoDFvYLyfBL5LlYL98lVOCN1N9iwrhUrqaTWQBHg7k%2Fo1tdC5k53GjUXtVG9%2FKJn5AyUbPoV'
    # url=r'http://p.yiqifa.com/n?k=2mLErnDS1NterI6H2mLErBXBYmul5cLq1n2s6mL7WNKqWn4H6EDmrI6HkQLErnXyWlwl3NwFrIW-&t=http://item.jd.com/10869637246.html'
    url=r'http://p.egou.com/n?k=2mLErnWFWlwLrI6H2mLErI6HWNRSWE4H6EKm6n4H6EDmrZU61BAgpmqerI6H353L6n3F15BH2L--&e=%user%&t=http://www.jd.com/'
    print getyiqifaurl(url)

