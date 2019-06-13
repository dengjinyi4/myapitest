#!/usr/bin/env python
# encoding: utf-8
import hashlib
import httplib
import json
def userlogin(site, ip, term, name,password,source,mtag):
    try:
        client = httplib.HTTPConnection("api.egou.com")
        url='rest?method=user.login&site=%d&ip=%s&term=%s&name=%s&password=%s&source=%s&mtag=%s'%(site, ip, term, name,password,source,mtag)
        print 'ok is url %r'%url
        client.request('GET',url)
        response = client.getresponse()
    except Exception, e:
        raise e
    finally:
        pass
    #print response.status
    result = response.read()
    print 'result'
    print result
    # value = json.loads(result)
    # print value
    # code = value["code"]
    return result


if __name__ == '__main__':
    code=userlogin(2,'192.168.0.1',6748583,'bbar','echere',111,1)
    print code



