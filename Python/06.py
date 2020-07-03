# 斐波那契数列。
#
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def fib(count):
    a, b = 0, 1
    while count > 0:
        yield a
        a, b = b, a + b
        count -= 1


if __name__ == '__main__':
    a = int(input('请输入一个整数（x>0）:'))
    for i in fib(a):
        print(i, end=' ')
