#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:Purchase.py
@time:2021/07/30
"""
import requests,time,json
from Config import test_host_cfg
import unittest
from API import login_api



#购买流程类
class Purchase_Process():
    def __init__(self):
        self.host = test_host_cfg.test_host
        a = ["GYS", 'YDK', 'YD']
        token_list=[]
        for num in a:
            token=login_api.Login_class().login(type=num)
            token_list.append(token)
        self.gys_token =token_list[0]
        self.ydk_token=token_list[1]
        self.yd_token=token_list[2]

        self.ydk_get_headers={"Authorization":self.ydk_token,
                              "source": "1"}
        self.gys_get_headers={"Authorization":self.gys_token}
        self.yd_get_headers = {"Authorization":self.yd_token}

        self.ydk_post_headers = {"Authorization":self.ydk_token,
                              "source": "1","Content-Type":"application/json"}

        self.gys_post_headers ={"Authorization":self.gys_token,
                                "Content-Type":"application/json"}

        self.yd_post_headers = {"Authorization":self.yd_token,
                                "Content-Type":"application/json"}


    #供应商和商店的用户信息
    def supper_shop_msg(self):
        pass

    #查看供应商是否具有商品(如果有，就返回商品信息；
    # 没有就调用创建商品的接口来创建商品，然后返回商品信息） 结果要断言
    def get_goods_for_supper(self):
        url=self.host+"/goods/no_auth/selectGoodsListSupplier"
        params = {"pageSize": 10,
                  "pageNum": 1}
        r=requests.get(url=url,params=params,headers=self.gys_get_headers)
        print(r.json())

    #供应商的商品详情
    def supper_goods(self,order_id="1412339836645879809"):
        url=self.host+"/goods/no_auth/selectGoodsAppById"
        data={"id":order_id}
        r=requests.post(url=url,data=json.dumps(data),headers=self.gys_post_headers)
        print(r.json())


    #供应商创建商品（返回商品信息） 结果要断言
    def creat_goods_for_supper(self):
        pass

    #查看供应商的商品列表，找出已经上架的商品，返回商品信息，结果要断言
    def goodslist_for_supper(self):
        url=self.host+"/goods/no_auth/selectGoodsListSupplier"#get
        params={"pageSize":10,
                "pageNum":1}
        r=requests.get(url=url,params=params,headers=self.gys_get_headers)
        print(r.json())





    #云档口获取自己的地址，结果要断言
    def get_shop_address(self):
        url=self.host+"/shop/getConsInfo"#get
        headers={"Authorization":self.ydk_token,
                 "source": "1"}
        r=requests.get(url=url,headers=headers)
        print(r.json())
        addressId=r.json()["data"][0]["consId"]
        print(addressId)
        return addressId





    #云档口选择供应商的商品来进行下单操作 ，结果要断言
    def creat_order_for_shop(self,addressId="1409329275076743168"):
        api="/order/info/create"#post
        data={"addressId":addressId,
              "orderInfo":[{"stallId":"4247513","orderGoods":
                  [{"goodsImg":"9bc706fcafbb4de.mp4",
                    "orderDetail":
                        [{"amount":1,"skuId":"TX211S0430003BCS"}]}]}],
              "orderSource":"APPLETS","orderType":"2"}



    #供应商接单,结果要断言（这步之后需要手动付款）
    def supper_order_receiving(self,purchaseId=""):
        url=self.host+"/purchase/receive"#post
        data={"purchaseId":purchaseId,"freightMoney":"0","supplierRemark":""}
        r=requests.post(url=url,data=json.dumps(data),headers=self.gys_token)
        print(r.json())



    #供应商发货，结果要断言
    def supper_deliver_goods(self):
        pass


    #云档口确认收货，结果要断言
    def shop_confirm_receipt(self):
        pass












if __name__ == '__main__':
    run=Purchase_Process()
    # run.goodslist_for_supper()
    run.supper_goods()