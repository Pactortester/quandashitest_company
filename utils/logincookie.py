
class dengLuPage:
    #url = "https://www.quandashi.com/"
    url = "https://www.quandashi.com/"


    cookie=({'name': 'QDS_COOKIE',
             'value': '116b79bb072221f47477b4c5980a685f0b4fa2d1',
              'Domain': '.quandashi.com'})

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def dengLu(self):
        self.open_page()
        self.driver.add_cookie(self.cookie)
        self.driver.refresh()

<<<<<<< HEAD
        self.driver.add_cookie({'name': 'QDS_COOKIE',
             #'value': '379e9613f3767a728fccbdd09cd4ae25575abb15', #线上
             'value': 'ab63c857c28ff94e241a578ecd1994ac520eece6',  #pre
             #'value': '72a184d1769150dc82e4649a2172b94d39f76e46',  #测试
              'Domain': '.quandashi.com'})
=======
    def refresh(self):
>>>>>>> 96013fa4116080cc88e432c305fdb48fec06a5d1

        self.driver.add_cookie(self.cookie)
        self.driver.refresh()





