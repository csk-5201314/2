#!/D:/csk/python
# -*-coding:utf-8-*-


import unittest
from config.HTMLTestRunner import HTMLTestRunner
import time
import os


#测试用例的路径
case_path=r"D:\csk\XM1\TestCase"  #路径只能到目录下，不能指定到文件
    #discover测试集，匹配在该路径下的以要运行脚本名开头的文件
discover=unittest.defaultTestLoader.discover(case_path,pattern="unit*.py")

if __name__ == '__main__':
    now=time.strftime("%Y %m %d %H %M %S")
    report=r"D:\csk\XM1\report_1"  #放报告的路径
    report_name=os.path.join(report,"%s.html" %(now))   #将文件名与路径连接起来  使用的now现在的时间
    with open(report_name,"wb") as file:
        runner=HTMLTestRunner(stream=file,
                              title=u"测试报告",
                              description=u"用例执行情况如下:",
                              tester=u"崔帅坤",
                              verbosity=2)  #0:不产生报告。 1:产生的报告不详细。2:产生的报告最详细
        run=HTMLTestRunner()
        runner.run(discover)
