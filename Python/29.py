# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。


a = int(input('请输入不多于5位的正整数(0<x<100000)：'))

if a <= 0 or a >= 100000:
    print('输入数字不符合要求')
else:
    b = str(a)
    print('%d是%d位数，逆序为%s' % (a, len(b), list(reversed(b))))



