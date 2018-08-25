# coding=utf-8
import random
import time

import logging

from utils.mytestcase import mytestcase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort


class znzztest(mytestcase):
    """智能注册测试集"""

    def test_znzz(self):
        """智能注册测"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#com-navbar > div > ul > li:nth-child(1) > a").click()
        time.sleep(1)
        self.assertIn("商标注册-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            #aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "test")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()
        # suiji11 = random.randint(2, 12)
        # suiji12 = random.randint(13, 24)
        # suiji13 = random.randint(25, 36)
        # suiji14 = random.randint(37, 46)


        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(10) > span").click()

        print("选择了第2类商标分类!")


        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div.last-pay > ul > li.row-step > a").click()

        time.sleep(1)
        #self.driver.execute_script("document.getElementByName('fname').length = 0;")

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "人才")
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        # driver.find_element_by_css_selector("#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span.list.active").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "一擦")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_xpath(
            "/html/body/div[6]/div[3]/div[2]/div[1]/table[2]/tbody[1]/tr[4]/td[2]/input").send_keys("03515978787")
        time.sleep(2)
        #解决常用申请人弹框，点击空白处
        self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[2]/h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.smartRegister-page div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz.png")

        for i in self.driver.find_elements_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):

            print("总价:"+i.text)
            ii=i.text

        #self.assertIn(aa,ii)
        #print("测试通过")
        #self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo=o.text

        self.assertIn(oo,ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()