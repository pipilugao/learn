# 一个5位数，判断它是不是回文数。

# 回文数，个位与万位相同，十位与千位相同。

a = int(input('请输入一个5位数：'))

if a > 9999 and a < 100000:
    b = str(a)
    c = ''.join(list(reversed(b)))
    if b == c:
        print('%d是回文数' % (a))
    else:
        print('%d不是回文数' % (a))
else:
    print('输入数字不符合要求')