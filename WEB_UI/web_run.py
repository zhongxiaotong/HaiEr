#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:web_run.py
@time:2021/07/08
"""
from selenium import webdriver
from Config import test_host_cfg
import time
from Common_Module import All_Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from ddt import ddt,data,file_data,unique
import unittest

excel_path=All_Common.Common_Parameter().get_excel_path(type="WEB")
run_get_vules=All_Common.Common_Parameter()
create_gys_vules=run_get_vules.get_excel(excel_path,"create_gys")

#登录页面元素
login_username="/html/body/div/div/div[1]/form/div[2]/div/div[1]/input"#登录用户名/手机号输入框
login_password="/html/body/div/div/div[1]/form/div[3]/div/div/input"#登录密码输入框
login_button="/html/body/div/div/div[1]/form/button"#登录按钮



#首页页面元素
GYS_GL="/html/body/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/a/li"#首页--》供应商管理
XZ_GYS="/html/body/div[1]/div/div[2]/section/div/form/div[2]/div/button[3]"#新增供应商按钮

#新增/编辑供应商
TJ_YYZZ="/html/body/div/div/div[2]/section/div/form/div[3]/div/div[2]/div[1]/input"#添加营业执照
GYS_QC="/html/body/div[1]/div/div[2]/section/div/form/div[4]/div/div[1]/input"#供应商全称
GYS_DQ_XL="/html/body/div[1]/div/div[2]/section/div/form/div[5]/div/div/div/span/span/i"#供应商地区下拉按钮
DQ_SF="/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]/span"#供应商地区省份选择“安徽省”
DQ_CS="/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[2]/span"#供应商地区城市选择“芜湖市”
DQ_dq="/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[4]/span"#供应商城市地区选择“三山区”
DQ_SSQ="/html/body/div[1]/div/div[2]/section/div/form/div[5]/div/div/div/input"#供应商地区城市选择"广东深/深圳市/宝安区"
DQ_XXDZ="/html/body/div[1]/div/div[2]/section/div/form/div[6]/div/div[1]/input"#详细地址
FR="/html/body/div[1]/div/div[2]/section/div/form/div[7]/div/div/input"#法人
TYSHXYDM="/html/body/div[1]/div/div[2]/section/div/form/div[8]/div/div/input"#统一社会信用代码
LXR="/html/body/div[1]/div/div[2]/section/div/form/div[10]/div/div[1]/input"#联系人
LXRDH="/html/body/div[1]/div/div[2]/section/div/form/div[11]/div/div/input"#联系人电话
YWLXRDH="/html/body/div[1]/div/div[2]/section/div/form/div[12]/div/div/input"#业务联系人电话
SQ_XL="/html/body/div[1]/div/div[2]/section/div/form/div[13]/div/div/div/span/span/i"#商圈下拉键
SQ_NY="/html/body/div[3]/div[1]/div[1]/ul/li[2]"#商圈选择--》南洋
QD="/html/body/div[1]/div/div[2]/section/div/div/button[2]"#确定



@ddt
class Web_Driver(unittest.TestCase):
    def setUp(self):
        self.host=test_host_cfg.test_HT_host
        self.WEB=webdriver.Firefox()
        self.WEB.implicitly_wait(15)#设置元素等待时间为5秒



    #登录
    def login(self):
        self.WEB.get(self.host)
        self.WEB.find_element_by_xpath(login_username).click()
        self.WEB.find_element_by_xpath(login_username).send_keys("17820512336")
        self.WEB.find_element_by_xpath(login_password).click()
        self.WEB.find_element_by_xpath(login_password).send_keys("123456")
        self.WEB.find_element_by_xpath(login_button).click()


    #创建供应商
    @data(*create_gys_vules)
    def test_creat_GYS(self,n_data):
        #登录
        self.login()
        #创建供应商流程
        self.WEB.find_element_by_xpath(GYS_GL).click()
        self.WEB.find_element_by_xpath(XZ_GYS).click()
        self.WEB.find_element_by_xpath(TJ_YYZZ).send_keys(r'C:\Users\Haier006\Desktop\测试图片\营业执照.jpg')
        self.WEB.find_element_by_xpath(GYS_QC).send_keys(n_data["gys_name"])
        self.WEB.find_element_by_xpath(GYS_DQ_XL).click()
        self.WEB.find_element_by_xpath(DQ_SF).click()
        self.WEB.find_element_by_xpath(DQ_CS).click()
        self.WEB.find_element_by_xpath(DQ_dq).click()
        # self.WEB.find_element_by_xpath(DQ_SSQ).send_keys("广东深/深圳市/宝安区")
        self.WEB.find_element_by_xpath(DQ_XXDZ).send_keys(n_data["address"])
        self.WEB.find_element_by_xpath(FR).send_keys(n_data["gys_name"])
        self.WEB.find_element_by_xpath(TYSHXYDM).send_keys(n_data["TYSHXYDM"])
        self.WEB.find_element_by_xpath(LXR).send_keys(n_data["gys_name"])
        self.WEB.find_element_by_xpath(LXRDH).send_keys(n_data["mobile"])
        self.WEB.find_element_by_xpath(YWLXRDH).send_keys(n_data["mobile"])
        self.WEB.find_element_by_xpath(SQ_XL).click()
        self.WEB.find_element_by_xpath(SQ_NY).click()
        # self.WEB.find_element_by_xpath(QD).click()
        time.sleep(5)

        #关闭浏览器
        self.close_web()



    def close_web(self):
        self.WEB.close()


if __name__ == '__main__':
    unittest.main()
    # run=Web_Driver()
    # run.login()
    # run.creat_GYS()
    # time.sleep(5)
    # run.close_web()