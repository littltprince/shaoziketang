import unittest
import BeautifulReport
from BeautifulReport import BeautifulReport
if __name__ == '__main__':
    suite = unittest.TestLoader().discover(start_dir=".",
                                           pattern="test_*.py",
                                           top_level_dir=None)


    BeautifulReport(suite).report(filename='测试报告',description='登录测试',log_path='.')