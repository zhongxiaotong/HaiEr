#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:send_email.py
@time:2021/06/30
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Common_Module import All_Common
from Config import email_cfg

class Email():

    def __init__(self):
        self.report_path=All_Common.Common_Parameter().get_report_path()



    # def yx_163(self):
    #     '''使用非QQ邮箱来发送邮件的方法'''
    #     #-----------1，跟发件相关的参数----------------
    #     smtpserver=''   #发件服务器
    #     port=0          #端口
    #     sender=''       #发送人的账号
    #     psw =''         #发送人的密码
    #     receiver =''    #接收人的邮箱账号
    #
    #     #------------2，编辑邮件的内容-----------------
    #     subject=''      #这个是邮件的主题
    #     body ='<p></p>' #定义邮件正文为html格式
    #     msg=MIMEText(body,"html",'utf-8')
    #     msg['from']=sender
    #     msg['to']=receiver
    #     msg['subject']=subject
    #
    #     #-----------3，发送邮件--------------------
    #     smtp=smtplib.SMTP()
    #     smtp.connect(smtpserver)  #链接服务器
    #     smtp.login(sender,psw)  #登录
    #     smtp.sendmail(sender,receiver,msg.as_string())#发送
    #     smtp.quit() #关闭
    #     print('邮箱发送成功')



    def yx_qq(self):



        '''使用QQ邮箱的方法'''
        smtpserver = "smtp.qq.com"
        port = 465  # 端口
        sender = email_cfg.sender # 账号
        psw = email_cfg.psw  # 密码
        receiver = email_cfg.receiver  # 接收人


        # ----------2.编辑邮件的内容------
        #读文件
        report_path=self.report_path
        # print(report_path)
        file_path=report_path
        with open(file_path,'rb')as fp:
            mail_body=fp.read()

        msg=MIMEMultipart()

        msg['from'] = sender#发件人
        msg['to'] = ",".join(receiver)#收件人
        msg['subject'] = "接口测试报告"#主题

        #正文
        body = MIMEText(mail_body,"html","utf-8")  # 定义邮件正文为 html 格式
        msg.attach(body)
        #!!!! # = MIMEText(body, "html", "utf-8")

        #附件
        att=MIMEText(mail_body,"base64","utf-8")
        att["Content-Type"]="application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att)

        # ----------3.发送邮件------

        smtp = smtplib.SMTP_SSL(smtpserver, port)        # 连服务器
        smtp.login(sender, psw)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        smtp.quit()  # 关闭
        print("QQ邮箱发送成功")



if __name__=="__main__":
    run=Email()

    run.yx_qq()