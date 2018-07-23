# coding=utf-8

import time

import logging

from utils.mytestcase import mytestcase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort

class hhrtest(mytestcase):

    """合伙人个人中心测试集"""

    def test_fwdd(self):
        """服务订单"""
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#com-header > div > div.item-right > ul.r-maps > li:nth-child(1) > a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalCenter2-header > div.header-box > div.header-box > div.header-nav > a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li.selected > a").click()
        self.driver.find_element_by_css_selector("#s-form > ul > li:nth-child(1) > input").send_keys("H80409275319")
        self.driver.find_element_by_css_selector("#s-form > ul > li:nth-child(8) > input").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > div.td-handle > a").click()
        time.sleep(3)
        """修改商标名字"""

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(4) > h2 > a").click()
        # self.driver.find_element_by_css_selector("#modal-brand > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("1")
        # self.driver.find_element_by_css_selector("#modal-brand > div.modal-button > a.button.save").click()
        print("商标名字修改成功")

        time.sleep(1)

        """修改尼斯分类"""
        self.driver.execute_script("window.scrollBy(0,4800)")  # 滑动滚动条



        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-categories > h2 > a").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > div > div > h4 > div.header-right > a > i").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child(2) > span").click()
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

        self.driver.find_element_by_css_selector("#edit-category > div.modal-button > a.button.cancel").click()
        print("尼斯分类修改成功")
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
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div.tabsPanel > ul > li.list.selected > a").click()
        print("渠道账号添加成功")

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(3) > div > dl > dt > input").send_keys("13910143379 / 2679745445@qq.com")
        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(4) > div.brandInfo-wrap > div.section-base > table > tbody > tr.row-name > td.td-content > input").send_keys("测试")
        self.driver.find_element_by_css_selector("#create-tuyang > label:nth-child(2) > i.iconfont.icon-danxuan").click()
        print("商标信息添加成功")

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(4) > div.brandInfo-wrap > div.section-base > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(4) > div.brandInfo-wrap > div.section-base > table > tbody > tr.row-way > td.td-content > a:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(4) > div.brandInfo-wrap > div.section-base > table > tbody > tr.row-industry1 > td.td-content > select.myInput.znfirst").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(4) > div.brandInfo-wrap > div.section-base > table > tbody > tr.row-industry1 > td.td-content > select.myInput.znfirst > option:nth-child(2)").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(4) > div.brandInfo-wrap > div.section-base > table > tbody > tr.row-industry1 > td.td-content > select.myInput.znsecond").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(4) > div.brandInfo-wrap > div.section-base > table > tbody > tr.row-industry1 > td.td-content > select.myInput.znsecond > option:nth-child(2)").click()
        print("尼斯分类添加成功")
        self.driver.execute_script("window.scrollBy(0,4800)")  # 滑动滚动条


        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(5) > div.agentInfo-wrap.agentInfo-wrap-in > div > table > thead > tr > td.td-content > a.btn-choice.fownertype.active").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(5) > div.agentInfo-wrap.agentInfo-wrap-in > div > table > tbody:nth-child(2) > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("文思海辉技术有限公司")
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector("#myadministrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#myadministrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(5) > div.agentInfo-wrap.agentInfo-wrap-in > div > table > tbody:nth-child(2) > tr:nth-child(4) > td.td-content > input").send_keys("蔡妍妍")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(5) > div.agentInfo-wrap.agentInfo-wrap-in > div > table > tbody:nth-child(2) > tr:nth-child(5) > td.td-content > input").send_keys("17801188216")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(5) > div.agentInfo-wrap.agentInfo-wrap-in > div > table > tbody:nth-child(2) > tr:nth-child(7) > td.td-content > input").send_keys("1132123@qq.com")
        print("申请人信息添加成功")


        #self.driver.find_element_by_class_name("btn btnupload").click()




        for i in self.driver.find_elements_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(6) > div > ul > li.row-sense > em"):
            print("应付总额：:"+i.text)
           # ii=i.text

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.section8 > div > a").click()

        get_screenshort(self.driver,"hhrsbzc.png")

        print("测试通过!")

