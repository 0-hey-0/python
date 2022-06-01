import json
import os
import sys
import unittest
from common.API_request import Test_requset

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

class Test_bus(unittest.TestCase):
    def setUp(self) -> None:
        self.api=Test_requset()
    def test_01_bus_list(self):
        self.api.test_api(filename="DemoAPITestCase.xlsx",module="出行服务")
    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
