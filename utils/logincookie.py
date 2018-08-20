
class dengLuPage:
    #url = "https://www.quandashi.com/"
    url = "https://pre-www.quandashi.com/"


    cookie=({'name': 'QDS_COOKIE',
             'value': '59d10186e2416ad0df8dd299085ed51d1c1c7753',
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





