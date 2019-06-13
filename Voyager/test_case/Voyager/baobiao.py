#encoding:utf-8
import requests
def guanggaoweiclick():
    r=requests.get("https://display.adhudong.com/spread/rotary-table.htm?logId=274174&adzoneId=1&actId=1&ref=")
    print r.status_code
    print r.text
guanggaoweiclick()