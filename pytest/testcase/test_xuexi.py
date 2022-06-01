# -*- coding:utf-8 -*-
import os

import pytest
import time
from importlib import reload
import sys



# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding="utf8",line_buffering=True)

# 主模式函数
#     （1）运行所有：pytest.main()
#     （2）指定模块：pytest.main(['-vs','test_xuexi.py'])
#     （3）指定目录：pytest.main(['-vs','./case'])
#     （4）通过nodeid指定用例运行：nodeid有模块名，分隔符，类名，方法名，函数名组成。
#         pytest.main(['-vs','./case/test_xuexi.py::TestXuexi::test_01_bailu'])
# 命令行模式
    # （1）运行所有：pytest
#     （2）指定模块：pytest -vs test_xuexi.py
#     （3）指定目录：pytest -vs ./case
#     （4）通过nodeid指定用例运行：nodeid有模块名，分隔符，类名，方法名，函数名组成。
#         pytest -vs ./case/test_xuexi.py::TestXuexi::test_01_bailu
# 参数详解：
#     -s:标识输出调试信息，包括print打印的信息
#     -v：显示更详细的信息
#     -vs：这两个参数一起用
#     -n：支持多线程或者分布式运行测试用例。
#         如：pytest -vs ./case/test_xuexi.py -n 2
#     --reruns NUM :失败用例重跑
#     -x：标识只要有一个用例报错就测试停止。
#     --maxfail=2  出现两个用例失败就停止。
#     -k：根据测试用例的部分字符串置顶用例。
#         如：pytest -vs ./case -k "ao"
#     --html ./report/report.html:生成html的测试报告
# 执行顺序：
#     默认从上到下的顺序
#     改变默认的执行顺序：使用mark标记：@pytest.mark.run(order=1)

# 通过读取pytest.ini配置文件运行
#     pytest.ini这个文件是pytest单元测试框架的核心配置文件。
#     1.位置：一般放在项目的根目录下
#     2.编码：必须是ASNI，可以使用notepad++修改编码格式
#     3.作用：改变pytest默认的行为
#     4.运行的规则：不管是主函数的模式运行还是命令模式，都会去读取这个配置文件
#     [pytest]
#     addopts=-vs               #命令行的参数，用空格分隔
#     testpaths-./case          #测试用例的路径
#     python_files=test_*.py    #模块名的规则
#     python_classes=Test*      #类名的规则
#     python_functions=test     #方法名的规则
# 分组执行（冒烟，分模块执行，分接口和web执行）
#     smoke：冒烟用例，分布在各个模块里面
#     pytest -vs -m "smoke"
#     pytest -vs -m "smoke or usermanage"
#     markers=
#         smoke:冒烟用例
#         usermanage:用户管理
# pytest跳过测试用例
#     （1）无条件跳过
#     @pytest.mark.skip(reason="用例跳过")
#     （2）有条件跳过
#     @pytest.mark.skipif(age>=18,reason="已成年")
# allure下载地址：https://github.com/allure-framework/allure2/releases
# 生成allure报告：os.system('allure generate ../temp -o ../report --clean')
# allure报告参数：
#     1、feature——测试用例特性（主要功能模块）：一般是在类上
#     2、story——feature功能模块下的分支功能：一般是在方法上
#     3、severity——测试用例的严重级别
#     4、step——测试用例的步骤
#     5、attach——用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
#     6、link/issue/testcase——链接
#     7、description——用例描述

# @pytest.fixture(scope="",params="",autouse="",ids="",name="")
# scope ：作用域
#     function，class，module，package/session

# @pytest.mark.parametrize(argnames='argsname',argvalues=argvalue)
# argsname:参数的名称
# argvalue:参数的值（列表[]，元组()，字典列表[{},{}]，字典元组({},{})），参数的值有多少个方法会执行多少次

# class TestXuexi:
#     age=18
#     def test_01_bailu(self):
#         # time.sleep(3)
#         print("测试白鹿")
#
#     @pytest.mark.run(order=1)
#     @pytest.mark.smoke
#     # @pytest.mark.skipif(age>=18,reason="已成年")
#     def test_02_baihe(self):
#         # time.sleep(3)
#         print("测试百合")
#
#     @pytest.mark.run(order=2)
#     # @pytest.mark.skip(reason="用例跳过")
#     def test_03_zhiliao(self):
#         # time.sleep(3)
#         print("测试知了")
#
#     @pytest.mark.usermanage
#     def test_04_bus(self):
#         # time.sleep(3)
#         print("测试公交")







