# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。


def fun(a):
    arr = []
    for i in range(2, a):
        if a % i == 0:
            arr.append(i)
    return arr


if __name__ == '__main__':
    arr = []
    for i in range(1, 1000):
        res = fun(i)
        if i == (sum(res) + 1):
            arr.append(i)

    print('1000以内完数有：', arr)