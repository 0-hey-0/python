import os
import sys
import json
import requests
from lib.request import request
import re
from config.readConfig import ReadConfig

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class API_Auth():
    def __init__(self,name):
        """
        引用方法，获取接口地址
        :param name:
        """
        cf=ReadConfig()
        self.host=cf.get_http(name)
        self.url_manage=self.host+"/api/basic/manage/auth/login"
        self.url_app=self.host+"/api/basic/app/auth/login"

    def get_manage_Auth(self,username,password):
        """
        登录后台获取并返回token
        :param username:
        :param password:
        :return:
        """
        data={
            "account":username,
            "password":password,
            "checkIp":False
        }
        header={
            "Content-Type":"application/json"
        }
        res=request(url=self.url_manage,data=data,header=header,method="post")
        # print(res)
        token = res["data"]
        print(token)
        return token
    def get_app_AUth(self,username,password):
        """
        登录APP获取token
        :param username:
        :param password:
        :return:
        """
        data={
            "mobile": username,
            "password": password
        }
        header={
            "Content-Type": "application/json"
        }
        res=request(url=self.url_app,data=data,header=header,method="post")
        # print(res)
        token=res["data"]
        print(token)
        return token



# a=API_Auth(name="url_c1")
# b=a.get_manage_Auth(username="heyu123",password="test1234")
# c=a.get_app_AUth(username="15196450437",password="test1234")