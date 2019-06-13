__author__ = 'emar0901'
import requests
if __name__ == '__main__':
    r=requests.get('http://www.baidu.com', stream=True)
    print r.encoding
    r.encoding='gbk'
    print r.raw.read()