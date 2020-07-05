# 求1+2!+3!+...+20!的和。


def fun(n):
    a = 1
    temp = 1
    while n > 0:
        yield '%d!' % a, temp
        a += 1
        temp *= a
        n -= 1

if __name__ == '__main__':
    a = []
    b = 0
    for i, j in fun(20):
        # print(i, j)
        a.append(i)
        b += j

    print(' + '.join(a), '=', b)
