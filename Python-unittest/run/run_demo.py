import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from lib.sendmail import send_mail
from lib.newReport import new_report
import case.test_travelManage

# 用例路径
case_path = os.path.join(os.path.abspath('..'),'case')
# 报告存放路径
report_path = os.path.join(os.path.abspath('..'), 'report')
# print(report_path)

def add_case():
    """加载所有的测试用例"""
    testunit=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*test_travelManage*.py", top_level_dir=None)
    # print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            # print(testunit)
    return testunit


def run_case(all_case):
    """执行所有的测试用例"""
    # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  report_path + '\\' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'接口自动化测试报告,测试结果如下：',description=u'用例执行情况：')
    runner.run(all_case)
    fp.close()
    report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    # print(report)
#     send_mail(report) #调用发送邮件模块

if __name__ =="__main__":
    run_case(add_case())




