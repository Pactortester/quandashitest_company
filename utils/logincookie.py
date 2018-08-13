import logging
from http.cookiejar import Cookie


class dengLuPage:
    #url = "https://www.quandashi.com/"
    url = "https://new.quandashi.com/"
    #url = "http://wwwtest-v1.quandashi.cn/"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def dengLu(self):
        self.open_page()

        self.driver.add_cookie({'name': 'QDS_COOKIE',
             'value': '54422abef9ce5761a8738a7213db4245cd197cb5', #线上
             #'value': 'a7b350758f326b637e56797234e1c81fc7e925fa',  #pre
             #'value': '72a184d1769150dc82e4649a2172b94d39f76e46',  #测试
              'Domain': '.quandashi.com'})

        self.driver.refresh()





