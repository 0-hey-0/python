import json
import os
import sys
import json
import requests
from lib.request import request
from lib.API_Authorization import API_Auth
from db.dbConnect import DB
from ddt import ddt, data, unpack

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


class Screen_Config():
    def __init__(self):
        Auth = API_Auth("url_test")
        self.token = Auth.get_manage_Auth(username="heyu123", password="test1234")
        Auth_hwy = API_Auth("url_huaweiyun")
        self.token_hwy = Auth_hwy.get_manage_Auth(username="heyu123", password="hy1519645")
        self.host = "https://test-bus-information.app-chengdu1.yunzhicloud.com"
        self.host_dev = "http://dev-bus-information.app-chengdu4.yunzhicloud.com"
        self.host_huaweiyun = "https://manager-information.cdgj-bus.com/"
        self.api_screenConfig = "/api/management/screen/device/screenConfig"
        self.api_pubtask = "/api/management/pub/task/bind"
        self.api_updatedevice = "/api/management/app/upgrade/devices"
        # self.db = DB(db_name="bus-information",env="test")
        # self.db_dev=DB(db_name="bus-information",env="dev")
        self.api_pubtask_dev = "/api/manage/task/pub"
        self.api_carno_get = "/api/management/car/page"
        self.api_serialno_update = "/api/management/car/device"

    def screenConfig(self, serial_no=None):
        """配置设备音量"""
        header = {
            "jwt-token": self.token
        }
        url = self.host + self.api_screenConfig
        if serial_no == None:
            sql = f"SELECT * FROM screen_device WHERE fd_deleted=0 AND fd_type=1;"
            device_res = self.db.qurey(sql=sql)
            devicelen = len(device_res) - 1
        else:
            sql = f"SELECT * FROM screen_device WHERE fd_deleted=0 AND fd_serial_no=\"{serial_no}\";"
            device_res = self.db.qurey(sql)
            devicelen = len(device_res)
        # print(device_res)
        screenConfig = {
            "enable": "true",
            "volume": 20,
            "light": 70
        }
        screenConfig_json = json.dumps(screenConfig).encode(encoding='utf-8')
        for i in range(0, devicelen):
            device_Id = device_res[i].get("fd_id")
            print(device_Id)
            update_data = {
                "deviceId": device_Id,
                "screenConfig": screenConfig_json
            }
            res = requests.put(url=url, data=update_data, headers=header, verify=False)
            print(res.json())

    def pub_taskreplace(self, serial_no=None, taskId=238):
        """更换节目"""
        header = {
            "jwt-token": self.token,
            "Content-Type": "application/json"
        }
        url = self.host + self.api_pubtask
        if serial_no == None:
            sql = f"SELECT * FROM screen_device WHERE fd_type=2 AND fd_deleted=0;"
            device_res = self.db.qurey(sql=sql)
            devicelen = len(device_res) - 1
        else:
            sql = f"SELECT * FROM screen_device WHERE fd_deleted=0 AND fd_serial_no=\"{serial_no}\";"
            device_res = self.db.qurey(sql)
            devicelen = len(device_res)
        # print(device_res)
        for i in range(0, devicelen):
            device_Id = device_res[i].get("fd_id")
            print(device_Id)
            update_data = {
                "deviceId": device_Id,
                "taskId": taskId
            }
            res = request(url=url, method="post", data=update_data, header=header)
            print(res)

    def update_devices(self, serial_no=None, type=1):
        """升级更新设备"""
        """屏类型：1.LED外屏、2.单面屏、3.互动屏、4.双面屏、5.LED广告屏、6.27寸单面屏"""
        url = self.host + self.api_updatedevice
        header = {
            "jwt-token": self.token,
            "Content-Type": "application/json"
        }
        # sql_task = f"SELECT * FROM app_upgrade;"
        # task_res = self.db.qurey(sql=sql_task)
        # # print(task_res)
        # taskId = task_res[-1].get("fd_id")
        if serial_no == None:
            sql_device = f"SELECT * FROM screen_device WHERE fd_type={type} AND fd_deleted=0;"
            device_res = self.db.qurey(sql=sql_device)
            devicelen = len(device_res) - 1
            print(devicelen)
        else:
            sql_device = f"SELECT * FROM screen_device WHERE fd_deleted=0 AND fd_serial_no=\"{serial_no}\";"
            device_res = self.db.qurey(sql_device)
            devicelen = len(device_res)
        # print(device_res)
        deviceId = []
        for i in range(0, devicelen):
            device_Id = device_res[i].get("fd_id")
            # print(device_Id)
            deviceId.append(device_Id)

        update_data = {
            "taskId": 62,
            "screenIds": deviceId
        }
        print(update_data)
        res = request(url=url, method="post", data=update_data, header=header)
        print(res)

    def grayscale_update_devices(self, type=1):
        """灰度升级设备"""
        """屏类型：1.LED外屏、2.单面屏、3.互动屏、4.双面屏、5.LED广告屏、6.27寸单面屏"""
        url = self.host + self.api_updatedevice
        header = {
            "jwt-token": self.token,
            "Content-Type": "application/json"
        }
        sql_device = f"SELECT * FROM screen_device WHERE fd_type={type} AND fd_deleted=0;"
        device_res = self.db.qurey(sql=sql_device)
        deviceId = []
        for i in range(0, 50):
            device_Id = device_res[i].get("fd_id")
            # print(device_Id)
            deviceId.append(device_Id)
        print(deviceId)
        update_data = {
            "taskId": 50,
            "screenIds": deviceId
        }
        print(update_data)
        res = request(url=url, method="post", data=update_data, header=header)
        print(res)

    def pub_taskreplace_dev(self, serial_no=None, type=21, taskId=238):
        """开发环境更换任务"""
        """20 25吋互动屏 、 21 27吋单面、22 32吋单面、23 32吋双面 、24  车外LED侧腰牌"""
        header = {
            "jwt-token": self.token,
            "Content-Type": "application/json"
        }
        url = self.host_dev + self.api_pubtask_dev
        if serial_no == None:
            sql_device = f"SELECT * FROM t_car_device WHERE fd_type={type} AND fd_deleted=0;"
            device_res = self.db_dev.qurey(sql=sql_device)
            devicelen = len(device_res) - 1
            print(devicelen)
        else:
            sql_device = f"SELECT * FROM screen_device WHERE fd_deleted=0 AND fd_serial_no=\"{serial_no}\";"
            device_res = self.db_dev.qurey(sql_device)
            devicelen = len(device_res)
        # print(device_res)
        deviceList = []
        for i in range(0, devicelen):
            device_Id = device_res[i].get("fd_id")
            device_serialNo = device_res[i].get("fd_serial_no")
            device_idserialNo = {
                "serialNo": device_serialNo,
                "id": device_Id
            }
            deviceList.append(device_idserialNo)
        print(deviceList)
        # update_data = {
        #     "detailList": [
        #         {
        #             "excDate": "2021-12-13",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-14",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-15",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-16",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-17",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-18",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-19",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-20",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-21",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-22",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-23",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-24",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-25",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-26",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-27",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-28",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-29",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-30",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2021-12-31",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-01",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-02",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-03",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-04",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-05",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-06",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-07",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-08",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-09",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-10",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-11",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-12",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-13",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-14",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-15",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-16",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-17",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-18",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-19",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-20",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-21",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-22",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-23",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-24",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-25",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-26",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-27",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-28",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-29",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-30",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         },
        #         {
        #             "excDate": "2022-01-31",
        #             "taskTemplateName": "绿色城市27寸图片",
        #             "taskTemplateId": 82
        #         }
        #     ],
        #     "deviceList": deviceList,
        #     "startTime": [
        #         "2021-12-12T16:00:00.000Z",
        #         "2022-01-30T16:00:00.000Z"
        #     ],
        #     "name": "绿色城市27寸图片",
        #     "deviceType": "SINGLE_SIDED_27",
        #     "startDate": "2021-12-13",
        #     "endDate": "2022-01-31"
        # }
        # res = request(url=url, method="post", data=update_data, header=header)
        # print(res)

    def serialno_carno_update(self, carNo, deviceId, serialNo, devicetype):
        """设备更换绑定车辆"""
        devicetypelist = {"27寸单": "SINGLE_SIDED_27", "32寸单": "SINGLE_SIDED_32", "32寸双": "DOUBLE_SIDED_27",
                          "25寸": "INTERACTIVE_SIDED_25", "侧腰牌": "CAR_OUT_LED", "广告牌": "CAR_OUT_LED_AD"}
        header_car = {
            "jwt-token": self.token_hwy
        }
        url_carnoget = self.host_huaweiyun + self.api_carno_get
        data_get = {
            "pageSize": 10,
            "pageNum": 1,
            "carNo": carNo
        }
        res_carNoget = request(url=url_carnoget, data=data_get, header=header_car, method="get")
        # print(res_carNoget)
        carId = res_carNoget["data"]["records"][0].get("id")
        # print(carId)
        header_devices = {
            "jwt-token": self.token_hwy,
            "Content-Type": "application/json"
        }
        data_devices = {
            "id": deviceId,
            "carId": carId,
            "serialNo": serialNo,
            "macCode": serialNo,
            "deviceScreenTypeEnum": devicetypelist[devicetype],
            "carNo": res_carNoget["data"]["records"][0].get("carNo"),
            "line": res_carNoget["data"]["records"][0].get("line"),
            "screenConfig": "{\"enable\":true,\"volume\":10,\"light\":100}",
            "companyId": res_carNoget["data"]["records"][0].get("companyId"),
            "remark": ""
        }
        # data = json.dumps(data_devices).encode(encoding='utf-8')
        # print(data_devices)
        url = self.host_huaweiyun + self.api_serialno_update
        res = request(url=url, data=data_devices, header=header_devices, method="put")
        print(res)


a = Screen_Config()
# b = a.screenConfig(serial_no="") ##配置设备音量
# c=a.pub_taskreplace(taskId=238) ##更换节目
# d = a.update_devices(serial_no="109aece6") ##升级设备
# f = a.pub_taskreplace_dev()
# car = a.serialno_carno_update(carNo="川A17128D", deviceId=2289, serialNo="10c70f0f", devicetype="侧腰牌")

# e=a.grayscale_update_devices(type=21)
