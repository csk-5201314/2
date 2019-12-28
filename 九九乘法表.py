#!/D:/csk/python
# - *-coding:utf-8-*-

"""
"""

"""
for循环打印九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (j, i, i * j), end="\t")
    print("")

"""
while循环打印乘法表
"""
# a = 1
# while a <= 9:
#     i = 1
#     while i <= a:
#         print("%d*%d=%d" %(i,a,a*i),end="\t")
#         i = i + 1
#     print("")
#     a = a + 1

