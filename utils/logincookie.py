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
              'value': '679b328b686905c5b148b5fc90f5db46cacf89a3', #一周有效期      mfsbtest.py
              'Domain': '.quandashi.com'})

        self.driver.refresh()





