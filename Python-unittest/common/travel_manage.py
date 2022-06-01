import json
import os
import sys
import json
import requests
from lib.request import request
from lib.API_Authorization import API_Auth
from config.readConfig import ReadConfig


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

buslinelist_API="/api/travel/manage/line/customize/page"


class Travel_manage():

    def __init__(self):
        Auth=API_Auth("url_c1")
        self.token=Auth.get_manage_Auth(username="heyu123",password="test1234")
        readCon=ReadConfig()
        self.host=readCon.get_http(name="url_test")

    def get_buslinelist(self):
        header={
            "Content-Type": "application/x-www-form-urlencoded",
            "jwt-token":self.token
        }
        url=self.host+buslinelist_API
        data={
            "pageNum":1,
            "pageSize":10
        }
        res=request(url=url,data=data,method="get",header=header)
        # print(res)
        return res







a=Travel_manage()
# b=a.get_buslinelist()
# print(b)
# code=b["data"]["records"]
# print(code)


