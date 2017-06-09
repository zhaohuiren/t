# coding=utf-8
import time
import unittest

from util.browser import Browser


class chuzhi(unittest.TestCase):
    def setUp(self):
    #初始化工作
        self.browser=Browser.BROWSER
        self.verificationErrors=[]
        #定义数组，脚本运行错误记录到这个数组里
        self.accept_next_alert=True
        #表示接受警告
    def test_1chuzhilogin(self):
        u"""处置登陆模块"""
        driver=self.browser
        driver.get("https://wj-01.zleida.com/login/login")
        driver.find_element_by_id("name").send_keys("cz-tongji")
        driver.find_element_by_id('password').send_keys('123456')
        driver.find_element_by_xpath("//input[contains(concat(' ', @class, ' '), ' btn ')]").click()
        title=driver.title
        self.assertEqual(title,"【工作平台】-资产雷达")


    def test_2chuzhi(self):
        u"""处置遍历模块"""
        driver=self.browser
        driver.get("https://wj-01.zleida.com/bid/select")
        title=driver.title
        self.assertEqual(title,"【委案获取】-资产雷达")
        driver.get("https://wj-01.zleida.com/bid")
        title=driver.title
        driver.get("https://wj-01.zleida.com/bid")
        self.assertEqual(title,"【委案列表】-资产雷达")
        driver.get("https://wj-01.zleida.com/settlement/getExceptionSettlementList")
        title=driver.title
        self.assertEqual(title,'【结算管理】-资产雷达')


    def test_3Settlement(self):
        u"""发起结算"""
        driver=self.browser
        driver.get('https://wj-01.zleida.com/bid?status=50')
        time.sleep(2)
        driver.find_element_by_xpath("//tr[1]//td[11]//a").click()
        driver.find_element_by_id('btn-pub').click()
        js="$('#settlementAmount').val('100')"
        driver.execute_script(js)
        driver.find_element_by_xpath("//input[contains(concat(' ', @class, ' '), ' btn ')]").click()
        text=driver.find_element_by_xpath("//div[contains(concat(' ', @class, ' '), ' alert-success ')]//p").text
        self.assertEqual(text,'催收进度申请成功，请等待委托方确认！')


    def test_4export(self):
        u"""导出"""
        driver=self.browser
        driver.get()





    def test_4quit(self):
        u"""退出"""
        driver=self.browser
        driver.get("https://wj-01.zleida.com//login/logout")



def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
