import logging
from http.cookiejar import Cookie


class dengLuPage:
    #url = "https://www.quandashi.com/"
    url = "https://pre-www.quandashi.com/"
    #url = "http://wwwtest-v1.quandashi.cn/"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def dengLu(self):
        self.open_page()

        self.driver.add_cookie({'name': 'QDS_COOKIE',
             #'value': '379e9613f3767a728fccbdd09cd4ae25575abb15', #线上
             'value': 'eeb4a8bdb397dc825880880119854c241b2b7679',  #pre
             #'value': '72a184d1769150dc82e4649a2172b94d39f76e46',  #测试
              'Domain': '.quandashi.com'})

        self.driver.refresh()





