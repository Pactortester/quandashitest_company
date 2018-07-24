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
              'value': '9868bc095607c5c8957d7d43b3d8c34b5c13d8e1', #一周有效期  2018-7-9_10-46    mfsbtest.py
              'Domain': '.quandashi.com'})

        self.driver.refresh()





