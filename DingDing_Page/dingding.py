#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:dingding.py
@time:2021/06/30
"""
import requests,json,time   #导入依赖库
from Config import dingding_cfg




class DingDing_Robot():
    def __init__(self):
        self.dingding_host=dingding_cfg.dingding_host
        self.dingding_token=dingding_cfg.dingding_token
        self.dingding_mobile=dingding_cfg.dingding_mobile
        self.dingding_mobile_2=dingding_cfg.dingding_mobile_2
        self.dingding_mobile_3 = dingding_cfg.dingding_mobile_3
        # self.dingding_mobile_4 = dingding_cfg.dingding_mobile_4



    def set_nwes(self,type=""):
        '''发送钉钉报警信息'''
        url=self.dingding_host+self.dingding_token
        # print(url)

        headers={'Content-Type': 'application/json'}   #定义数据类型
        if type=="failfast":
        #定义要发送的数据
            data ={
                "msgtype": "text",
                "text": {
                    "content": "测试报警：这是第二种测试警报"#监控的接口出现问题，请后台和测试查看一下测试报告，已发送报告到邮箱"
                },
                "at": {
                    "atMobiles": [self.dingding_mobile,
                                  self.dingding_mobile_2,
                                  self.dingding_mobile_3
                    ],
                    "isAtAll": False}}
            data_1=json.dumps(data)
            # print("阶段1")
            r=requests.post(url=url,data=data_1,headers=headers)
            # print(r.text)


        elif type=="errors":
            data = {
                "msgtype": "text",
                "text": {
                    "content": "测试报警：这是第一种测试报告"#自动化脚本代码错误，请速度查看"
                },
                "at": {
                    "atMobiles": [self.dingding_mobile,
                                  self.dingding_mobile_2,
                                  self.dingding_mobile_3
                                  ],
                    "isAtAll": False}}
            data_1 = json.dumps(data)
            # print("阶段2")
            r = requests.post(url=url, data=data_1, headers=headers)
            # print(r.text)


        elif type=="two":
            data = {
                "msgtype": "text",
                "text": {
                    "content": "测试报警：这个是三种测试警报"#接口和自动化脚本代码都出现了错误，请后台和测试都查看一下测试报告"
                },
                "at": {
                    "atMobiles": [self.dingding_mobile,
                                  self.dingding_mobile_2,
                                  self.dingding_mobile_3
                                  ],
                    "isAtAll": False}}
            data_1 = json.dumps(data)
            # print("阶段3")
            r = requests.post(url=url, data=data_1, headers=headers)
            # print(r.text)

        else:
            print("没有这个选择")






if __name__=="__main__":
    run=DingDing_Robot()
    # run.set_nwes()
    for a in range(3):
        run.set_nwes(type="failfast")
        time.sleep(1)
    nwes_list=["failfast","errors","two"]
    for num in nwes_list:
        run.set_nwes(type=num)
        time.sleep(3)

    # run_1=Dingding_Robot_new()
    # run_1.getMedia_id()
    # run_1.SendFile()   #发送测试报告到钉钉群上面