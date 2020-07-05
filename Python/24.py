# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前20项之和。


def fun(n):
    a, b = 1, 2
    while n > 0:
        # print(b / a)
        yield '%d/%d' % (b, a)
        a, b = b, a + b
        n -= 1

if __name__ == '__main__':
    arr = []
    a = 0
    for i in fun(20):
        arr.append(i)
        a += eval(i)

print(' + '.join(arr), '=', eval('+'.join(arr)))
print(a)
