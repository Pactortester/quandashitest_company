
class dengLuPage:
    #url = "https://www.quandashi.com/"
    url = "https://new.quandashi.com/"

    cookie=({'name': 'QDS_COOKIE',
             'value': '4cee3ae144733628cc3ce396a7713a2cfe720901',
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





