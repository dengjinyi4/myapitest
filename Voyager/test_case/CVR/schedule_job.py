# encoding=utf-8
__author__ = 'aidinghua'
import schedule
import time


def job():

    print "I'm working...."

#schedule.every().hour.do(cvr.cvr())
# schedule.every(1).minutes.do(job)
# schedule.every(1).seconds.do(job)
schedule.every().day.at("13:28").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("15:30").do(job)

while True:

    schedule.run_pending()

    time.sleep(1)