#!/D:/csk/python
# -*-coding:utf-8-*-

import unittest
import os
import time
from config.HTMLTestRunner import HTMLTestRunner
from common.AndroidHelper import Helper,driver
import logging
import logging.config


class Study_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig()
        cls.Helper=Helper()

    @classmethod
    def tearDownClass(cls):
        cls.Helper.quit()

    def setUp(self):#每条用例执行之前都会执行一次
        print("每条用例执行前，我会先执行")

    def test02(self):
        logging.info("截屏正常")
        self.Helper.save_screenshot()

    def test03(self):
        self.Helper.denglu()

    def tearDown(self):  #每条用例执行之后我才会执行一次
        print("每条用例执行之后我才会执行一次")


if __name__ == '__main__':
    unittest.main()



