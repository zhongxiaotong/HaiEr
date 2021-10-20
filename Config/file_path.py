#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZXT
@file:file_path.py
@time:2021/06/30
"""
'''所有文件路径的存储文件'''
import requests, json, time,yaml
from Common_Module import All_Common



class Path_cls():
    def __init__(self):
        self.path=All_Common.Common_Parameter().projects_path()


    def get_yml(self):
        path_dict=yaml.safe_load(open(self.path+r"\Config\file_path.yml","r",encoding="utf-8"))
        return path_dict


if __name__ == '__main__':
    run=Path_cls()
    run.get_yml()