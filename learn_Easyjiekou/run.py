import unittest
from BeautifulReport import BeautifulReport
from config import *
from
import logging

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)  # 从配置文件中读取用例路径

with open(report_file, 'wb') as f:  # 从配置文件中读取
    BeautifulReport(stream=f, title="Api Test", description="测试描述").run(suite)

send_email(report_file)  # 从配置文件中读取
logging.info("================================== 测试结束 ==================================")