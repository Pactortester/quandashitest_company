import unittest
import time

from  selenium import  webdriver

class mytestcase(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\\Administrator\\AppData\Local\\Google\Chrome\\Application\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()