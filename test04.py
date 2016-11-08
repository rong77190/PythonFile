# encoding:UTF-8
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于3时需考虑多加一天：

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
a = [0,31,59,90,120,151,181,212,243,273,304,334]
if (year % 400 ==0) or (year % 4==0) or (year % 100 != 0):
    if (month < 2):
        strHello = "这是第 %d 天" % ( a[month-1]+day)
        print(strHello)
    else:
        strHello = "这是第 %d 天" % (a[month - 1] + day +1)
        print(strHello)
else:
    strHello = "这是第 %d 天" % (a[month - 1] + day)
    print(strHello)

