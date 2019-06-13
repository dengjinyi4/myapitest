__author__ = 'emar0901'
import requestegouchaojifan
def getjdurl(url):
    id=requestegouchaojifan.getyiqifaurl(url).split('&utm_campaign=t_')[1].split('_')[1]
    return id
    pass
def getjd360buyurl(url):
    id=requestegouchaojifan.getyiqifaurl(url).split('&utm_campaign=t_')[1].split('_')[1].split('&')[0]
    return id
    pass
if __name__ == '__main__':
    jdurl=r'http://p.egou.com/n?k=2mLErnWFWlwLrI6H2mLErI6HWNRSWE4H6EKm6n4H6EDmrZU61BAgpmqerI6H353L6n3F15BH2L--&e=%user%&t=http://www.jd.com/'
    print  getjdurl(jdurl)