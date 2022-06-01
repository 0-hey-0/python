import allure
import pytest

from utils import yaml_util

from utils.request import request

host = yaml_util.read_config()[1]["url_c1"]

@allure.epic("成都公交项目")
@allure.feature("登录模块")
class TestAuth:
    '''
    测试后台和app登录模块
    '''

    @allure.story('后台用户登录')
    # @allure.title("后台用户登录")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(host,name="后台接口地址：{}".format(host))
    @allure.step('后台测试登录成功获取token')
    @pytest.mark.parametrize(argnames='arg_manage', argvalues=yaml_util.read_yaml(yaml_name="get_token_manage.yaml"))
    def test_01_manageAuth(self, arg_manage):
        # print(arg_manage)
        with allure.step('1.输入用户名：{}  2.输入密码：{}  3.点击登录'.format(arg_manage["request"]["data"].get("account"),
                                                              arg_manage["request"]["data"].get("password"))):
            manage_url = host+arg_manage["request"].get("url")
            manage_method = arg_manage["request"].get("method")
            manage_data = arg_manage["request"].get("data")
            manage_header = arg_manage["request"].get("header")
            allure.attach(body=arg_manage["request"].get("url"), name="请求接口",
                          attachment_type=allure.attachment_type.TEXT)
            print("打印：",manage_header,manage_url,manage_data,manage_method)
            manage_res = request(method=manage_method, url=manage_url, data=manage_data, header=manage_header)
            print(manage_res)
            if manage_res.get("data"):
                yaml_util.clear_yaml()
                yaml_util.write_yaml({"manage-token":manage_res.get("data")})


    @allure.story('APP用户登录')
    # @allure.title("APP用户登录")
    @allure.link(host, name="APP接口地址：{}".format(host))
    @allure.step('APP测试登录成功获取token')
    @pytest.mark.parametrize(argnames='arg_app', argvalues=yaml_util.read_yaml(yaml_name="get_token_app.yaml"))
    def test_02_appAuth(self,arg_app):
        # print(arg_app)
        with allure.step('1.输入手机号：{}  2.输入密码：{}  3.点击登录'.format(arg_app["request"]["data"].get("mobile"),
                                                              arg_app["request"]["data"].get("password"))):
            app_url = host + arg_app["request"].get("url")
            app_method = arg_app["request"].get("method")
            app_data = arg_app["request"].get("data")
            app_header = arg_app["request"].get("header")
            allure.attach(body=arg_app["request"].get("url"), name="请求接口",
                          attachment_type=allure.attachment_type.TEXT)
            # print("打印：", app_header, app_url, app_data, app_method)
            app_res = request(method=app_method, url=app_url, data=app_data, header=app_header)
            print(app_res)
            if app_res.get("data"):
                yaml_util.write_yaml({"app-token":app_res.get("data")})