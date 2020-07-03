# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
#
# 兔子的规律为数列1,1,2,3,5,8,13,21....

def fib(month):
    a, b = 1, 1
    while month > 0:
        yield a
        a, b = b, a + b
        month -= 1

if __name__ == '__main__':
    a = int(input('请输入月数（x>0）：'))

    for i in fib(a):
        print(i, end=' ')