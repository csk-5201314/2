#!/D:/csk/python
# -*-coding:utf-8-*-
""""""
from selenium import webdriver  # 导入模块内的网页驱动功能
import time


"""打开浏览器，请求网址"""
dr = webdriver.Firefox()  # 选择浏览器   python路径下安装的是什么webdriver，就输入什么浏览器（第一个字母大写）
dr.get("https://www.baidu.com")

"""web函数，断言：判断预期结果与执行结果是否一致。获取当前网页的标题和url"""
# dr.get("https://www.baidu.com")
# print(dr.title)  # 获取当前页面的标题
# assert dr.title == "百度一下，你就知道"
#
# print(dr.current_url)  # 获取当前页面的url
# assert dr.current_url == "https://www.baidu.com/"

"""设定浏览器窗口打开时的大小"""
# dr.maximize_window()  # 最大化浏览器窗口
# time.sleep(3)
# dr.minimize_window()  # 最小化浏览器窗口(即：将窗口隐藏到任务栏)

"""设定浏览器打开窗口时固定大小"""
# dr.set_window_size(1000,800)   #  （x轴，y轴）  以屏幕的最左上角为0.0的点打开窗口
#
# dr.set_window_position(400,400)  #以左上角0.0点为原点，x轴向右400，y轴向下400的点，为窗口打开的起始点

"""网页回滚"""
# dr.get("https://www.baidu.com")
# time.sleep(3)
# dr.get("https://www.jd.com")
# dr.back()
# time.sleep(3)
# dr.forward()
# time.sleep(3)
# dr.back()

"""关闭浏览器，能否打开多个窗口由网站的服务器决定"""
# time.sleep(5)
# # dr.quit() #彻底的退出浏览器  关闭所有窗口
# dr.close() #关闭浏览器的一个窗口    当浏览器打开的有多个窗口时，关闭当前操作的窗口

"""定位方式一共八种   ①id   ②class_name  ③name(在selenium中name对应的是网页中name的值，和appium中的name不同)  """
"""id"""
# dr.get("https://mail.qq.com")
# dr.switch_to.frame("login_frame")
# time.sleep(5)
# dr.find_element_by_class_name("inputstyle").send_keys("1269031826@qq.com")
# time.sleep(3)
# dr.find_element_by_id("p").click()
# dr.find_element_by_id("p").send_keys("密码")
# time.sleep(3)
# dr.find_element_by_id("login_button").click()
"""④xpath定位 路径标记语言"""
# dr.get("https://mail.qq.com")
# dr.switch_to.frame("login_frame")
# time.sleep(5)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys("1269031826@qq.com")
# dr.find_element_by_xpath('//*[@id="p"]').send_keys("密码")
# dr.find_element_by_xpath('//*[@id="login_button"]').click()


"""⑤tag_name 标签定位：用于list定位"""

"""⑥link_text  通过文本来定位(文本内容必须唯一)"""
# dr.find_element_by_link_text("新闻").click()#定位百度首页上的“新闻”文本
#
"""⑦partil_link_text(模糊文本定位 文本内容必须唯一)"""
# dr.find_element_by_partial_link_text("hao")  #例：定位百度首页内的    hao123
#
"""⑧css选择器 定位  by_css_selector   火狐定位内容右键css定位器"""
dr.find_element_by_css_selector("a.mnav:nth-child(2)").click()  #通过css选择器定位 hao123




