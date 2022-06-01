
import os
import pytest











if __name__ == '__main__':
    pytest.main()
    # os.system('allure generate ./temp -o ./report --clean')


# if __name__ == '__main__':
#     conf = Configs.Config()
#     log = Log.MyLog()
#     log.info('初始化配置文件, path=' + conf.conf_path)
#
#     shell = Shell.Shell()
#
#     # exp: 异地启动报告
#     cmd2 = 'pytest -s -q  --alluredir  allure_report --clean-alluredir'
#     cmd3 = 'allure serve allure_report'
#
#     try:
#         os.chdir(r"./testcase")  # 跳到报告路径下
#         print(os.getcwd())
#         shell.invoke(cmd2)
#         shell.invoke_2(cmd3)
#         # log.info(shell.invoke_2(cmd3))
#     except Exception:
#         log.error('异地启动失败，请检查环境配置')
#         raise
#     else:
#         log.info("没有执行")