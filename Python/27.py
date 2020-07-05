# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def fun(a):
    n = len(a)
    if n == 1:
        return a
    return a[-1] + fun(a[:n-1])


if __name__ == '__main__':
    a = 'asd123'
    print(a, fun(a))