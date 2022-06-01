import allure
import pytest

from utils import yaml_util
from utils.request import request

host = yaml_util.read_config()[1]["url_information_c1"]

@allure.epic("成都公交项目")
@allure.feature("信息发布模块")
class TestInformationManage:
    '''
    信息发布
    '''

    @allure.story('车辆管理')
    @allure.title("添加车辆")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(host, name="后台接口地址：{}".format(host))
    @allure.step('后台测试成功添加车辆')
    @pytest.mark.parametrize(argnames='arg_manage', argvalues=yaml_util.read_yaml(yaml_name="car_add.yaml"))
    def test_01_car_add(self,arg_manage):
        with allure.step('1.输入车辆信息{}  2.点击提交'.format(arg_manage["request"]["data"])):
            url=host+arg_manage["request"].get("url")
            method = arg_manage["request"].get("method")
            data = arg_manage["request"].get("data")
            header = arg_manage["request"].get("header")
            token=yaml_util.read_ex_yaml()
            print(token)
            update_header=dict(header,**token)
            allure.attach(body=arg_manage["request"].get("url"), name="请求接口",
                          attachment_type=allure.attachment_type.TEXT)
            print("打印：", update_header, url, data, method)
            res = request(method=method, url=url, data=data, header=update_header)
            print(res)

    def test_02_car_delete(self):
        pass

