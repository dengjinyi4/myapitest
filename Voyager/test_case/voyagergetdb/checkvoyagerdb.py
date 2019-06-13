#encoding: utf-8
__author__ = 'jinyi'
import db,checkconfig
check=checkconfig.checkconfig()
def getykhb():
    r=db.selectsql('devvoyager',check.cheykhbsql())
    tmpstr=u'''5:预扣款划拨是:{} 6:预扣款回款是:{}'''.format(str(r[0][1]),str(r[1][1]))
    if abs(r[0][1])-abs(r[1][1])>=check.ykhbcount:
        return False,tmpstr
    else:
        return True,tmpstr

if __name__ == '__main__':
    print getykhb()