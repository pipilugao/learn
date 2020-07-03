# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#
#从2开始找，被整除后，继续从从该数开始找，直到整除后商为1时，结束分解

b = a = int(input('请输入一个正整数(x>0)：'))
arr = []

while a != 1:
    pri = 2
    for i in range(pri, a+1):
        if a % i == 0:
            a //= i
            arr.append(str(i))
            pri = i
            break

print(b, '=', '*'.join(arr), sep='')