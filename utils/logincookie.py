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
              'value': '131ebc3888a47f7cff16e7a2f6532ab306c96156', #一周有效期  2018-7-9_10-46    mfsbtest.py
              'Domain': '.quandashi.com'})

        self.driver.refresh()





