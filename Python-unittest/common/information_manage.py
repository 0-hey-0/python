import json
import os
import sys
import random
import json
import requests

from lib.random_carNo import random_carNo
from lib.request import request
from lib.API_Authorization import API_Auth
from config.readConfig import ReadConfig

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

carlist_api = "/api/management/car/page"
caradd_api = "/api/management/car"
linecarlist_api="/api/management/car/line-car-list"
linegrouplist_api="/api/management/car/line-group-list"


class Information_manage():

    def __init__(self):
        Auth = API_Auth("url_c1")
        self.token = Auth.get_manage_Auth(username="heyu123", password="test1234")
        readCon = ReadConfig()
        self.host = readCon.get_http("url_information_c1")
        self.header = {
            "jwt-token": self.token
        }

    def car_list(self, data=None):
        url = self.host + carlist_api
        update_data = {
            "pageNum": 1,
            "pageSize": 10
        }
        if data != None:
            update_data = dict(update_data, **data)
        res = request(url=url, method="get", data=update_data, header=self.header)
        # print(res)
        return res

    def car_add(self, data=None):
        header = {
            "Content-Type": "application/json"
        }
        update_header = dict(self.header, **header)
        carNo=random_carNo(num=1,first="川",second="A",energy="New",cartype="large")[0]
        update_data = {
            "carTypesEnum": "BELL_BELL_CAR_12",
            "carModel": "12m",
            "carNo": carNo,
            "line": "100",
            "motorcade": "100",
            "remark": "",
            "stationStatusEnum": "OPERATING"
        }
        if data != None:
            update_data = dict(update_data, **data)
        url = self.host + caradd_api
        res = request(url=url, data=update_data, header=update_header, method="post")
        print(res)
        return res

    def car_update(self, data=None):
        header = {
            "Content-Type": "application/json"
        }
        update_header = dict(self.header, **header)
        carlist_res = self.car_list()
        carId = carlist_res["data"]["records"][0].get("id")
        carNo = carlist_res["data"]["records"][0].get("carNo")
        update_data = {
            "id": carId,
            "carTypesEnum": carlist_res["data"]["records"][0].get("carTypesEnum"),
            "carModel": carlist_res["data"]["records"][0].get("carModel"),
            "carNo": carNo,
            "line": carlist_res["data"]["records"][0].get("line"),
            "motorcade": carlist_res["data"]["records"][0].get("motorcade"),
            "remark": "auto_update",
            "stationStatusEnum": carlist_res["data"]["records"][0].get("stationStatusEnum")
        }
        if data != None:
            update_data = dict(update_data, **data)
        update_data = json.dumps(update_data).encode(encoding='utf-8')
        url = self.host + caradd_api
        print(update_data)
        res = request(url=url, data=update_data, header=update_header, method="put")
        print(res)
        return res

    def car_delete(self,data=None):
        carlist_res = self.car_list()
        carId = carlist_res["data"]["records"][0].get("id")
        update_data = {
            "id": carId
        }
        if data != None:
            update_data = dict(update_data, **data)
        url = self.host + caradd_api
        res = request(url=url, data=update_data, header=self.header, method="delete")
        print(res)
        return res

    def car_details(self,data=None):
        car_res=self.car_list()
        update_data={
            "id":car_res["data"]["records"][0].get("id")
        }
        if data != None:
            update_data = dict(update_data, **data)
        url=self.host+caradd_api
        res=request(url=url,data=update_data,header=self.header,method="get")
        print(res)
        return res

    def line_group_list(self,data=None):
        url=self.host+linegrouplist_api
        res=request(url=url,data=data,header=self.header,method="get")
        print(res)
        return res

    def line_car_list(self,data=None):
        url=self.host+linecarlist_api
        linegroup_res=self.line_group_list()
        lineNamelist=linegroup_res["data"]
        print(lineNamelist)
        index=random.randint(0,len(lineNamelist)-1)
        print(index)
        lineNa=lineNamelist[index]["lineName"]
        update_data={
            "lineNameList":[lineNa]
        }
        if data != None:
            update_data = dict(update_data, **data)
        res=request(url=url,data=update_data,header=self.header,method="get")
        print(res)
        return res



if __name__ == '__main__':
    inf = Information_manage()
    # inf.car_list()
    # inf.car_add()
    # inf.car_update()
    # inf.car_delete()
    # inf.line_group_list()
    # inf.line_car_list()
    # inf.car_details()