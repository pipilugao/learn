# 输入某年某月某日，判断这一天是这一年的第几天？
#
# 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天。

import re

year = int(input('请输入年份(0-inf eg:2019):'))
# month = int(input('请输入月份：0-12 2'))
# day = int(input('请输入月份：0-31 02'))

while year <= 0:
    year = int(input('请输入年份(0-inf eg:2019):'))
