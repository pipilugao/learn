# 利用递归方法求5!。

def fun(n):
    if n == 1:
        return 1
    return n * fun(n-1)


if __name__ == '__main__':
    print('5!=', fun(5))