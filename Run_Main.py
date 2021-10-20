#!/user/bin/python3
# -*- coding: UTF-8 -*-
"""
@File:Run_Main.py
@Description:描述
@Author:ZXT
@Date:2021/01/25
"""
import requests, json, time
'''用来执行所有的测试ceas'''


import unittest
from Common_Module import All_Common

import HTMLTestRunner
from Log_Page import test_log
from Config import email_cfg
from  Email_Page import send_email
from DingDing_Page import dingding



case_dir=All_Common.Common_Parameter().get_test_case_path()

def all_case():
    # 待执行用例的目录

    testcase=unittest.TestSuite()

    discover=unittest.defaultTestLoader.discover(case_dir,
                                                 pattern="test*.py",
                                                 top_level_dir=None)

    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            testcase.addTest(test_case)


    return testcase



if __name__ == "__main__":

    log = test_log.Log()

    log.info('测试开始')

    # print("现在是第%s次监控接口数据"%cishu)
    report_path =All_Common.Common_Parameter().get_report_path()
    fp = open(report_path, "wb")

    # stream:测试报告的内容要写入那个文件
    # title:测试报告的主题
    # description:测试报告的描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'测试报告',
                                           description=u'测试用例执行情况')
    r = runner.run(all_case())
    print("r.failures===",r.failures)
    print("r.errors===",r.errors)
    print("r.failfast===",r.failfast)

    if r.failures != []:
        print("报错了啊！！看着办")
        log.warning("发送钉钉警报")
        dingding.DingDing_Robot().set_nwes(type="failfast")
        put_youxiang = send_email.Email().yx_qq()
        log.warning('测试结束')


    elif r.errors != []:
        print("接口代码级别错误，请查看一下")
        log.warning("发送钉钉警报")
        put_youxiang = send_email.Email().yx_qq()
        log.warning('测试结束')
        dingding.DingDing_Robot().set_nwes(type="errors")




    elif r.failfast !=False:
        print("接口报错，自动化代码也报错，请查看")
        log.warning("发送钉钉警报")
        put_youxiang = send_email.Email().yx_qq()
        log.warning('测试结束')
        dingding.DingDing_Robot().set_nwes(type="two")


    else:
        print()
        print("测试通过，所有测试用例准确无误")



