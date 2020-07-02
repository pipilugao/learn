# 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
# 在10000内判断

import math

for i in range(10000):
    a = math.sqrt(i + 100)
    b = math.sqrt(i + 268)
    if a % 1 == 0 and b % 1 == 0:
        print(i)