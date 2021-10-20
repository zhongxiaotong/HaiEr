#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:test_log.py
@time:2021/06/30
"""
import requests, json, time
import os
import time
import logging
from Common_Module import All_Common


log_path=All_Common.Common_Parameter().get_log_path()
class Log():
    def __init__(self):
        #文件的命名
        self.logname=os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter=logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')



    def console(self,level,message):
        #创建一个FileHandler,用于写到本地
        fh=logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创建一个StreamHandler,用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level =="info":
            self.logger.info(message)
        elif level =="debug":
            self.logger.debug(message)
        elif level =="warning":
            self.logger.warning(message)
        elif level =="error":
            self.logger.error(message)
        #这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()


    def debug(self,message):
        self.console("debug",message)

    def info(self,message):
        self.console("info",message)

    def warning(self,message):
        self.console("warning",message)

    def error(self,message):
        self.console("error",message)




if __name__=="__main__":
    log=Log()
    log.info("-----测试开始----")
    log.info('输入密码')
    log.warning("测试结束")


