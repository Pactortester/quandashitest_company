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
              'value': '8cf92a5f3d7ecd1b68462f4b8c95391052c3efe3', #一周有效期      mfsbtest.py
              'Domain': '.quandashi.com'})

        self.driver.refresh()





