# encoding:UTF-8
# 题目:古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

# def f1(n):
#     if(n ==1 or n ==2):
#         return 1
#     else:
#         return f1(n-1) + f1(n-2)
#
# i = int(input("总几个月\n"))
# for index in range(1,i+1):
#     print(f1(index))

import MySQLdb