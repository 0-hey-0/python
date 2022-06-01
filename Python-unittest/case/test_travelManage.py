import json
import os
import sys
import json
import unittest
from lib.request import request
from lib.API_Authorization import API_Auth
from config.readConfig import ReadConfig
from common.travel_manage import Travel_manage

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

class Test_travelManage(unittest.TestCase):

    def setUp(self) -> None:
        self.travel=Travel_manage()
    def test_01_bus_lineList(self):
        res=self.travel.get_buslinelist()
        code=res.get("code")
        records=res["data"]["records"]
        self.assertEqual(code,200)
        self.assertIsNotNone(records)
    def tearDown(self) -> None:
        pass



if __name__ == '__main__':
        unittest.main()

