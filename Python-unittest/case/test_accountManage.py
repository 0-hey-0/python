import json
import os
import sys
import json
import unittest
from lib.request import request
from lib.API_Authorization import API_Auth
from config.readConfig import ReadConfig
from common.account_manage import Account_manage
from db.dbConnect import DB

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)



class Test_accountManage(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account_manage()
        #连接数据库
        self.db = DB(db_name="bus-basic",env="c1")
        global roleId

    def test_01_account_add(self):
        """添加账号"""
        depart_res = self.account.get_departlist()
        # print(depart_res)
        depart_id = depart_res.get("data")[-1].get("id")
        # print(depart_id)
        role_res = self.account.get_rolelist()
        # print(role_res)
        global roleId
        role_id = role_res.get("data")[-1].get("id")
        roleId=role_id
        # print(role_id)
        #请求添加账号接口
        res = self.account.account_add(depart_id=depart_id, role_id=role_id)
        print(res)
        #断言
        self.assertEqual(res.get("code"), 200)
        self.assertEqual(res.get("success"), True)

    def test_02_account_update(self):
        """修改账号"""
        account_res = self.account.get_accountpage()
        account_id = account_res.get("data").get("records")[0].get("id")
        print(account_id)
        res = self.account.account_update(account_id=account_id)
        print(res)
        #断言
        self.assertEqual(res.get("code"), 200)
        self.assertEqual(res.get("success"), True)

    def test_03_account_delete(self):
        """删除账号"""
        account_res = self.account.get_accountlist()
        # print(account_res)
        account_id = account_res.get("data")[-1].get("id")
        # print(account_id)
        # global roleId
        print("打印：",roleId)
        res = self.account.account_delete(account_id=account_id)
        print(res)
        self.assertEqual(res.get("code"), 200)
        self.assertEqual(res.get("success"), True)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
