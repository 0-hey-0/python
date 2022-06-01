import json
import os
import sys
import json
import requests
from lib.request import request
from lib.API_Authorization import API_Auth
from config.readConfig import ReadConfig
import random
from db.dbConnect import DB

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
account_add_api = "/api/basic/manage/manager"
role_list_api = "/api/basic/manage/role/list"
depart_list_api = "/api/basic/manage/organization/tree_list"
account_page_api = "/api/basic/manage/manager/page"
account_list_api = "/api/basic/manage/manager/list"


class Account_manage():
    def __init__(self):
        """
        引用方法，连接数据库，获取接口环境地址
        """
        Auth = API_Auth(name="url_c1")
        #获取token
        self.token = Auth.get_manage_Auth(username="heyu123", password="test1234")
        readCon = ReadConfig()
        #获取接口环境地址
        self.host = readCon.get_http(name="url_c1")
        #连接db
        self.db = DB(db_name="bus-basic", env="c1")

    # ------角色配置------
    def get_rolelist(self):
        """角色下拉列表"""
        header = {
            "jwt-token": self.token
        }
        url = self.host + role_list_api
        #请求角色下拉列表接口
        res = request(url=url, method="get", header=header)
        # print(res)
        return res

    # -------组织架构-------
    def get_departlist(self):
        """组织下拉列表"""
        header = {
            "jwt-token": self.token
        }
        url = self.host + depart_list_api
        # print(url)
        #请求组织下拉列表接口
        res = request(url=url, method="get", header=header)
        print(res)
        return res

    # ---------账号管理-------

    def account_add(self, depart_id, role_id, data=None):
        """添加账号"""
        header = {
            "jwt-token": self.token,
            "Content-Type": "application/json"
        }
        url = self.host + account_add_api
        update_data = {
            "account": "autotest",
            "cellphone": "1321231" + str(random.randint(1000, 9999)),
            "orgIds": [depart_id],
            "name": "autotest",
            "password": "test1234",
            "roleId": [role_id],
            "roleIds": {
                "ids": [role_id]
            },
            "status": 1
        }
        #判断传入data是否为空，不为空追加到update_data里
        if data != None:
            #追加参数到update_data里
            update_data = dict(update_data, **data)
        # print(update_data)
        #请求添加账号接口
        res = request(url=url, data=update_data, method="post", header=header)
        print(res)
        return res

    def get_accountpage(self, data=None):
        """账号列表"""
        header = {
            "jwt-token": self.token
        }
        url = self.host + account_page_api
        update_data = {
            "pageNum": 1,
            "pageSize": 10
        }
        if data is not None:
            update_data = dict(update_data, **data)
        #请求添加账号接口
        res = request(url=url, data=update_data, method="get", header=header)
        # print(res)
        return res

    def get_accountlist(self):
        """账号下拉列表"""
        header = {
            "jwt-token": self.token
        }
        url = self.host + account_list_api
        #请求账号下拉列表接口
        res = request(url=url, method="get", header=header)
        # print(res)
        return res

    def account_update(self, account_id, data=None):
        """账号修改"""
        header = {
            "jwt-token": self.token,
            "Content-Type": "application/json"
        }
        url = self.host + account_add_api
        sql = f"select * from t_manager m,t_manager_ref_role r where m.fd_id=r.fd_user_id AND m.fd_id={account_id}"
        #执行SQL
        accountdb_res = self.db.qurey(sql=sql)
        # print(accountdb_res)
        role_id = accountdb_res[0].get("fd_role_id")
        update_data = {
            "account": accountdb_res[0].get("fd_account"),
            "cellphone": accountdb_res[0].get("fd_cellphone"),
            "departId": accountdb_res[0].get("fd_depart_id"),
            "name": "autotest" + str(random.randint(0, 9999)),
            "id": account_id,
            "roleId": [
                role_id
            ],
            "roleIds": {
                "ids": [
                    role_id
                ]
            },
            "status": 1
        }
        if data is not None:
            update_data = dict(update_data, **data)
        # update_data = json.dumps(update_data).encode(encoding='utf-8')
        res = request(url=url, method="put", data=update_data, header=header)
        print(res)
        return res

    def account_delete(self, account_id):
        """账号删除"""
        header = {
            "jwt-token": self.token,
            "Content-Type": "application/json"
        }
        url = self.host + account_add_api
        data = {
            "ids": [
                account_id
            ]
        }
        # data = json.dumps(data).encode(encoding='utf-8')
        res = request(url=url, method="delete", data=data, header=header)
        print(res)
        return res


a = Account_manage()
# b=a.get_rolelist()
# b=a.get_departlist()
# data={
#     "account":"autotest001"
# }
# c=a.account_add(depart_id=214,role_id=105,data=data)
# d=a.get_accountpage()
# b=a.get_accountlist()
# b=a.account_update(account_id=104)
# b=a.account_delete()
