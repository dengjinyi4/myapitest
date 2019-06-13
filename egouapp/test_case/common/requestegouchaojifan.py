#!/usr/bin/env python
# encoding: utf-8
import requests,urllib
def get_taobaourl(url):
    # get t_js url
    refer=requests.get(url).url
    print refer
    headers={'Referer':refer}
    # get taobaourl
    taobaourl=requests.get(urllib.unquote(refer.split('tu=')[1]),headers=headers).url
    print taobaourl
    # taobaourl=requests.get(urllib.unquote(refer.split('tu=')[1]),headers=headers).url.split('&ali_trackid=')[0]
    return taobaourl.split(':')[2]
    pass
if __name__ == '__main__':
    url=r'http://s.click.taobao.com/t?e=m%3D2%26s%3DZv4XM38ktmgcQipKwQzePOeEDrYVVa64K7Vc7tFgwiG3bLqV5UHdqcSFQIOmuwQ0%2Fl0%2B1yuzCtIdNuy53hxY1wzMJkyv%2FlYULZArbCKs%2FKZxtvjBelf7FGnGvue0APvul%2BRNs72y5wAcCw7duA63ByJE62tYeVyxh9TbKRs8zk5nxPc1cu1A9U%2BqW2iPnV6dNFhZbezFL1pYC7K2OdchcA%3D%3D'
    print get_taobaourl(url)

