#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:app_run.py
@time:2021/07/08
"""
import uiautomator2 as u2
from cmd import Cmd
import os
class App_Drive():
    def __init__(self):
        pass

    def get_devices(self):
        order_str="adb devices"
        device=os.system(order_str)
        print(type(device))

    # def open

if __name__ == '__main__':

    run=App_Drive()
    run.get_devices()
