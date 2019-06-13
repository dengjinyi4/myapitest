#encoding:utf-8
__author__ = 'jinyi'
import datetime
class checkconfig:
    # 当天的预扣划拨差异
    ykhbcount=200
    # 检查当天的预扣划拨是否相等
    def cheykhbsql(self):
        # 检查当天的预扣划拨sql
        checkhbhksqltmp='''SELECT type,sum(amount) from voyager.advertiser_balance_log where change_time>='{}' and change_time<'{}' and type in (5,6) GROUP BY type ORDER BY id desc; '''
        checkhbhksqltmp=checkhbhksqltmp.format(self.tmpdaylist(1),self.tmpdaylist(0))
        print checkhbhksqltmp
        return checkhbhksqltmp
    # 获得日期
    def tmpdaylist(self,days):
        d = datetime.datetime.now()
        tmpdate_from=d+datetime.timedelta(days=-int(days))
        tmpdate_from=str(tmpdate_from)[0:10]
        daylist=tmpdate_from
        return daylist


if  __name__ == '__main__':
    check=checkconfig()
    print check.cheykhbsql()

