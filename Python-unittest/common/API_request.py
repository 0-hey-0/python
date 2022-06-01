import os
import sys
import json
import requests
from lib.request import request
from lib.API_Authorization import API_Auth
from config.readConfig import ReadConfig
from config.ReadExcel import ReadExcel
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


class Test_requset():
    def __init__(self):
        Auth = API_Auth(name="url_c1")
        self.token = Auth.get_manage_Auth(username="heyu123", password="test1234")
        readCon = ReadConfig()
        self.host = readCon.get_http(name="url_test")
        self.test = unittest.TestCase()

    def test_api(self, filename, module):
        SOURCE_FILE = os.path.join(BASE_DIR, "database", filename)
        self.readexcel = ReadExcel(fileName=SOURCE_FILE)
        excellist = self.readexcel.read_data()
        print(excellist)
        for i in range(0, len(excellist) - 1):
            excel_module = excellist[i].get("Module")
            if module == excel_module:
                API = excellist[i].get("API")
                print(API)
                code = excellist[i].get("Status_code")
                method = excellist[i].get("Method")
                excel_header = excellist[i].get("header")
                excel_header = json.loads(excel_header)
                # print(excel_header)
                data = excellist[i].get("data")
                expect_res = excellist[i].get("Expected results")
        new_header = {"jwt-token": self.token}
        header = dict(new_header, **excel_header)
        # print(header)
        url = self.host + API
        res = request(url=url, data=data, method=method, header=header)
        # print(res)
        self.test.assertEqual(res.get("code"), code)
        self.test.assertEqual(res.get("success"), True)

        return res, expect_res

a=Test_requset()
b,c,d=a.test_api(module="出行服务",filename="DemoAPITestCase.xlsx")
print(c)
