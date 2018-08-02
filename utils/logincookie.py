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
              'value': '035cc1479d4441604e565dc30d9234a21309a98b', #一周有效期      mfsbtest.py
              'Domain': '.quandashi.com'})

        self.driver.refresh()





