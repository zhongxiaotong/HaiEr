#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:login_api.py
@time:2021/07/01
"""
'''这个文档里面放入了一些项目的请求接口，比如登录'''

import time,requests,json
from Config import test_host_cfg,api_login_cfg,test_telephone_cfg
from Common_Module import All_Common



class Login_class():
    def __init__(self):
        self.host=test_host_cfg.test_host
        self.YDK_api=api_login_cfg.YDK_api
        self.GYS_api=api_login_cfg.GYS_api
        self.YD_api=api_login_cfg.YD_api
        self.HT_api=api_login_cfg.HT_api
        self.telephone=test_telephone_cfg.test_telephone
        self.password=test_telephone_cfg.password

    #获取云档口、云店、供应商的token，type=YDK获取云档口的token，type=GYS获取供应商的token，type=YD获取云店的token
    def login(self,type="YDK"):
        data={"telephone":self.telephone}
        if type=="YDK":
            api=self.YDK_api
        elif type=="YD":
            api = self.YD_api
        elif type=="GYS":
            api = self.GYS_api
        r = requests.post(url=self.host + api, data=json.dumps(data))
        if type=="GYS":
            token="Bearer "+r.json()["data"]["token"]
        else:
            token="Bearer "+r.json()["data"]
        # print(r.json())
        print(token)
        return token


    #大数据后台获取token
    def get_console_token(self):
        api=self.HT_api
        payload='username={}&password={}'.format(self.telephone,self.password)
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'dev-cloud-stall-manage-front.haier-ioc.com'}#请求头是必须的，不然无法正常登录

        r=requests.post(url=self.host+api,headers=headers,data=payload)
        token="Bearer "+r.json()["data"]
        print(token)
        return token





if __name__ == '__main__':
    run=Login_class()
    a=['YDK','YD']
    for num in a :
        run.login(type=num )

