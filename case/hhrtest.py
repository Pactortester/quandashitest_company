# coding=utf-8
import random
import time

import logging

from utils.mytestcase import mytestcase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort

class hhrtest(mytestcase):

    """合伙人个人中心测试集"""

    def test_sbdd(self):
        """商标订单"""
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#com-header > div > div.item-right > ul.r-maps > li:nth-child(1) > a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalCenter2-header > div.header-box > div.header-box > div.header-nav > a").click()

        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()

        self.driver.find_element_by_css_selector("#s-form > ul > li:nth-child(1) > input").send_keys("H80724472157")
        self.driver.find_element_by_css_selector("#s-form > ul > li:nth-child(8) > input").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(2) > td:nth-child(9) > div.td-handle > a").click()
        time.sleep(3)
        """修改商标名字"""

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(4) > h2 > a").click()
        # self.driver.find_element_by_css_selector("#modal-brand > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("1")
        # self.driver.find_element_by_css_selector("#modal-brand > div.modal-button > a.button.save").click()
        print("商标名字修改成功")

        time.sleep(1)

        """修改尼斯分类"""
        self.driver.execute_script("window.scrollBy(0,4200)")  # 滑动滚动条

        suiji = random.randint(2, 46)

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-categories > h2 > a").click()



        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > div > div > h4 > div.header-right > a > i").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        self.driver.find_element_by_css_selector("#edit-category > div.modal-button > a.button.save").click()
        print("尼斯分类修改为第{}类".format(suiji-1))
        time.sleep(1)

        """申请人信息"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.applicant-info > h2 > a").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > table > thead > tr:nth-child(1) > td.td-content > a:nth-child(2)").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("田伟")
        self.driver.find_element_by_css_selector("#geren-idCard").clear()
        self.driver.find_element_by_css_selector("#geren-idCard").send_keys("140121198906311532")
        self.driver.find_element_by_css_selector("#personalssq").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-button > a.button.save").click()
        print("申请人信息修改成功")
        time.sleep(4)

        """订单联系人"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(8) > div > h2 > a").click()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys("大西瓜")
        self.driver.find_element_by_css_selector("#change-contact-info > div.modal-button > a.button.save").click()

        print("订单联系人修改成功")
        time.sleep(1)

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-fix > div > div.right > div.pay-btns > a").click()
        get_screenshort(self.driver,"fwddtest.png")

        #self.driver.find_element_by_css_selector("#layui-layer100001 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        print("测试通过!")




    def test_hhrsbzc(self):

        """合伙人商标注册"""
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#com-header > div > div.item-right > ul.r-maps > li:nth-child(1) > a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalCenter2-header > div.header-box > div.header-box > div.header-nav > a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li:nth-child(2) > ul > li:nth-child(1) > a").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("大佬")
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()

        print("商标名称填写成功!")

        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别"""
        suiji=random.randint(1,46)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类".format(suiji))

        for i in self.driver.find_elements_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.order-categories > div.order-categories-total > span.span-total > strong > i"):
            print("总价:"+i.text)
            ii=i.text

        """申请人信息"""
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/table/thead/tr[1]/td[2]/a[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"overseastype\"]/label[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/div/div/div/table[1]/tbody[1]/tr[1]/td[2]/dl/dt/input").send_keys("文思海辉技术有限公司")
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()

        print("申请人信息填写成功!")


        """客户联系人信息"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys("dalao")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys("15624992488")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys("1456470136@qq.com")

        print("联系人信息填写成功!")


        """订单备注"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S")+"测试订单")

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()


        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a:nth-child(2)").click()

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo=o.text

        self.assertIn(oo,ii)

        self.driver.find_element_by_css_selector("#payways > li:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver,"hhrtest.png")

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap > div.paying-sk-button > a.button.send").click()

        print("订单已发送客户付款!")







