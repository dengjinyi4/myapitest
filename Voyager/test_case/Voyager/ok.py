#!/usr/bin/env python
#encoding: utf-8
import unittest,requests,sys
from bs4 import BeautifulSoup
import os
# hostandport=sys.argv[1]
# print hostandport

if __name__ =='__main__':
    # print hostandport
    # unittest.main()
	#testunit = unittest.TestSuite()
    re=requests.session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept - Encoding':'gzip, deflate, br',
               'Accept-Language':'zh-CN,zh;q=0.8',
               'upgrade-insecure-requests':'1',
               'cookie':'webp=1; __jdv=122270672|direct|-|none|-|1549935119557; autoOpenApp_downCloseDate_auto=1549935122282_21600000; sc_width=1366; shshshfpa=bedd5645-43a8-be0e-3fed-089902a8c411-1549935128; mt_xid=V2_52007VwMWV1VQUF4fSRFYAWADF1FfUFtbF0ARbAxlBBYCXVgFRk9BHQkZYlARUkEIB18dVRtUAGAGEABYDABSFnkaXQVvHxNRQVhRSx5BEl4DbAEWYl9oUmocQRBZAmQCE1ptWFteFw%3D%3D; warehistory="13300150265,18663737076,"; wq_logid=1549937173.1477513537; wxa_level=1; retina=1; cid=9; __jda=122270672.15499351195561423980989.1549935119.1549935119.1549935119.1; __jdb=122270672.6.15499351195561423980989|1.1549935119; __jdc=122270672; mba_muid=15499351195561423980989; mba_sid=1549935119558621240017412450.6; __wga=1549937174318.1549935123271.1549935123271.1549935123271.6.1; visitkey=2978561369713178; PPRD_P=UUID.15499351195561423980989-CT.37287.1.1-LOGID.1549937174330.99247816; sk_history=13300150265%2C; shshshfp=30d629981ae5e7c7ce14c81a40ccdb16; shshshsID=7918c8b31ecd9a5a5a1e830da6c847e0_5_1549937175028; shshshfpb=05ed344f6e2cb5646e1921e689b6e4ce7aab01da260a975db5bea92054',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    payload = {
        "authority": "item.m.jd.com",
        "path": "/product/13300150265.html",
        "scheme": "https"
    }
    url='https://item.m.jd.com/product/13300150265.html'
    result=re.get(url,headers=headers)
    soup =BeautifulSoup(result.text,'html.parser')
    all_img= (soup.find('i', class_='mod_tag').find_all('img'))
    print all_img

    # result=re.get(url,headers=headers)
    # re.headers.update(headers)
    # result=re.get(url,params=payload)
    print all_img