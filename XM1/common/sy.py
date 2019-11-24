#!/D:/csk/python
# -*-coding:utf-8-*-
import time
from selenium.webdriver.support.ui import WebDriverWait
import logging.config
import logging
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import yaml
import csv

# 安装包名：com.tencent.qqlive
# activity名：com.tencent.qqlive/.ona.activity.HomeActivity

with open(r"D:\csk\XM1\config\capability.yaml", 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
desired_cap = {'platformName': data["platformName"],
               'platformVersion': data["platformVersion"],
               'deviceName': data["deviceName"],
               'appActivity': data["appActivity"],
               'appPackage': data["appPackage"],
               'noReset': data["noReset"],
               'unicodeKeyboard': data["unicodeKeyboard"],
               'resetKeyboard': data["resetKeyboard"],
}

driver = webdriver.Remote("http://127.0.0.1:4723/wb/hub",desired_cap)

def tiaoguo():
    try:
        # 将服务器启动地址的变量driver赋予给lambda，并规定显性等待3秒只要等待的元素出现，就点击这个元素
        # 相当于  driver.find_element_by_id("com.tal.kaoyan:id/tv_skip").click()
        WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/tv_skip"))
        driver.get_screenshot_as_file("../report/跳过.png")
        driver.find_element_by_id("com.tal.kaoyan:id/tv_skip").click()
        driver.find_element_by_id('com.tal.kaoyan: id / tip_commit').click()
    except:
        print("跳过那个点")
    else:
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/tip_commit"))
        driver.find_element_by_id("com.tal.kaoyan:id/tip_commit").click()
        driver.get_screenshot_as_file("../report/同意权限.png")
        driver.find_element_by_id('com.tal.kaoyan: id / tip_commit').click()


def denglu():
    try:
        driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').click()
        driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys("乐以忘忧520")
        driver.get_screenshot_as_file("../report/用户名.png")
        driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys("aaazzz123")
        driver.get_screenshot_as_file("../report/密码.png")
        driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

    except:
        print("登录时发生错误")

tiaoguo()
denglu()


















