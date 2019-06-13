import unittest,hdtapi,sys,api_admin
# from nose_parameterized import parameterized, param
from parameterized import  parameterized
import myparamtest
myid=1
def totalDetail():
    s=api_admin.adminlogin()
    tmpname=sys._getframe().f_code.co_name
    allcase=hdtapi.getparam_db(tmpname)
    tmplist=[]
    for i in allcase:
        tmpdup=()
        para=eval(i[2])
        result=s.get(str(i[1]),params=para)
        tmpdup=i[0],result.json()['code'],i[3],i[4],
        tmplist.append(tmpdup)
    print tmplist
    return tmplist
class TestAdd(myparamtest.ParametrizedTestCase):

    @parameterized.expand(totalDetail)
    def testapi2(self,casename,str_val,expected,type):
        print 'oooooooooooooooooo'
        print self.param
        print str_val
        print expected
        if str(str_val)==str(expected):
            print 111111110000000999999
        print 'oooooooooooooooooo'
        if str(type)=='B':
            self.assertEqual(str(str_val),str(expected))
        else:
            print 11111
    def setUp(self):
        global myid
        print '3333333333333333'
        print self.param
        myid=self.param
        myid=+2
        print myid
        print( '444444444444444444444')
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAdd('testapi2'))
    # suite.addTest(myparamtest.ParametrizedTestCase.parametrize(TestAdd, param=1023))
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()