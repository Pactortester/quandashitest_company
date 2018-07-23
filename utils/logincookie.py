import logging
from http.cookiejar import Cookie


class dengLuPage:
    url = "https://pre-www.quandashi.com/"


    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def dengLu(self):
        self.open_page()

        self.driver.add_cookie({'name': 'QDS_COOKIE',
              'value': 'aa59bbaba7bfb56c8ed490b76a8196dd7c67b3ed', #一周有效期  2018-7-9_10-46    mfsbtest.py
              'Domain': '.quandashi.com'})

        self.driver.refresh()





