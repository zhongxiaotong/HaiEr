import time,requests,json
from Config import test_host_cfg,api_login_cfg,test_telephone_cfg
from Common_Module import All_Common
import pymysql


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
        # print(token)
        return token


    def gys_token(self):
        token=self.login(type="GYS")
        api="/purchase/selectAllBySupplierIdOfApp?pageSize=50&pageNum=1&orderStatus=WAIT_PAYMENT"
        headers={"Authorization":token,
                 "cource":"3",
                 "content-type":"application/x-www-form-urlencoded"}
        r=requests.get(url=self.host+api,headers=headers)
        # print(r.json())
        # time.sleep(1000)
        all_order=r.json()["data"]["records"]
        order_lis=[]
        for num in all_order:
            # print(num)
            # print(num["orderId"])
            order_lis.append(num["orderId"])

        # print(order_lis)
        return order_lis



    # 根据self.host取的环境，来切换现在的数据库的环境
    def get_mysql_host(self):
        mysql_host = "h2.haier-ioc.com"
        mysql_uesr = 'developer'
        mysql_password = "developer2020.YStest"
        mysql_db = "cloud_stall_test"
        mysql_port = 3306
        # 数据库连接，返回连接对象
        conn = pymysql.connect(host=mysql_host, user=mysql_uesr, password=mysql_password, db=mysql_db, port=mysql_port)

        return conn


    # 所有sql语句的公用模块
    def all_sql(self, sql_str):
        conn = self.get_mysql_host()
        cursor = conn.cursor()
        cursor.execute(sql_str)
        conn.commit()
        r = cursor.fetchall()
        cursor.close()
        conn.close()
        return r

    def update_order_status(self):
        # order_list=self.gys_token()
        # id=order_list[0]
        # print("现在要修改的订单id是:{}".format(id))
        # order_len=len(order_list)
        # print("现在还有剩余{}个订单".format(order_len-1))
        order_list=["CG1428650232526278657"]
        for id in order_list:
            sql_str="""UPDATE ys_order_info SET pay_method="WECHAT",pay_money="189",order_status="WAIT_SHIP",pay_time="2021-8-20 00:00:000" where order_id="{}"  """.format(id)
            self.all_sql(sql_str)
            print(111)



    def ydk_token(self):
        token=self.login(type="YDK")
        api="/order/info/create"
        data={"addressId":"${addressId}",
              "orderInfo":[{"stallId":"${suppId}","orderGoods":
                  [{"goodsImg":"${imgUrl}","orderDetail":
                      [{"amount":1,"skuId":"${skuCode}"}]}]}],
              "orderSource":"APPLETS","orderType":"2"}


    def get_mysql(self):
        sql_str="select * from  ys_shop_info where contact_phone='17820512336'"
        r=self.all_sql(sql_str)
        # print(r)
        # print(time.sleep(10000))
        # print("!!!!!!!!!!!!")
        # print()
        shopId=r[0][0]
        # print(shopId)
        return shopId

    def get_mysql_02(self):
        print("这个是第二个方法调用的")
        num=self.get_mysql()
        print(num)


if __name__ == '__main__':
    run=Login_class()
    # for a in range(20):
    run.get_mysql_02()