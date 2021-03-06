
# coding=utf-8

import time

import logging

from selenium.webdriver import ActionChains

from utils.mytestcase import mytestcase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort


class yytrtest(mytestcase):
    """异议他人商标测试集"""

    def test_sbcs(self):
        """商标撤三测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
<<<<<<< HEAD
            "#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > h3 > a")).perform()
=======
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
>>>>>>> 96013fa4116080cc88e432c305fdb48fec06a5d1
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > div > dl:nth-child(4) > dd > a:nth-child(1)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标撤三申请-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys("test")

        get_screenshort(self.driver, "test_sbcs.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_sbyy(self):
        """商标异议申请测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
<<<<<<< HEAD
            "#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > h3 > a")).perform()
=======
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
>>>>>>> 96013fa4116080cc88e432c305fdb48fec06a5d1
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > div > dl:nth-child(4) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标异议申请-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys("test")

        get_screenshort(self.driver, "test_sbyy.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_sbwx(self):
        """商标无效宣告申请测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
<<<<<<< HEAD
            "#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > h3 > a")).perform()
=======
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
>>>>>>> 96013fa4116080cc88e432c305fdb48fec06a5d1
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > div > dl:nth-child(4) > dd > a:nth-child(3)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标无效宣告申请-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys("test")

        get_screenshort(self.driver, "test_sbwx.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()