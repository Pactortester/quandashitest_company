
class dengLuPage:
    #url = "https://www.quandashi.com/"
    url = "https://new.quandashi.com/"

    cookie=({'name': 'QDS_COOKIE',
             'value': '5c13cb37731c9241169910271a743a1c18105d7e',
              'Domain': '.quandashi.com'})

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def dengLu(self):
        self.open_page()
        self.driver.add_cookie(self.cookie)
        self.driver.refresh()

    def refresh(self):

        self.driver.add_cookie(self.cookie)
        self.driver.refresh()





