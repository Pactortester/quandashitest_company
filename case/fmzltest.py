# coding=utf-8

import time

import logging

from utils.mytestcase import mytestcase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort


class fmzltest(mytestcase):
    """发明专利测试集"""

    def test_fmzl_1(self):
        """基础型-单个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#com-navbar > div > ul > li:nth-child(2) > a").click()
        self.assertIn("发明专利申请基础型_权大师",self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]").click()  #单个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2) > input[type=\"checkbox\"]")  #多个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector("body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()


        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys("test")

        get_screenshort(self.driver, "test_fmzl_1.png")

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


    def test_fmzl_2(self):
        """基础型-多个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#com-navbar > div > ul > li:nth-child(2) > a").click()
        self.assertIn("发明专利申请基础型_权大师",self.driver.title)
        print(self.driver.title)
        #self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2) > input[type=\"checkbox\"]").click()  #多个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector("body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()


        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys("test")

        get_screenshort(self.driver, "test_fmzl_2.png")

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


    def test_fmzl_3(self):
        """基础型-不减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#com-navbar > div > ul > li:nth-child(2) > a").click()
        self.assertIn("发明专利申请基础型_权大师",self.driver.title)
        print(self.driver.title)
        #self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2) > input[type=\"checkbox\"]")  #多个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]").click() #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector("body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()


        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys("test")

        get_screenshort(self.driver, "test_fmzl_3.png")

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