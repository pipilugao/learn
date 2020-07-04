# 求s=a+aa+aaa+aaaa+aa...a的值，
# 其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

a = int(input('请输入一个数字：'))
n = int(input("请输入几个数相加："))

c = 0
temp = a
arr = []

for i in range(n):
    c += temp
    arr.append(temp)
    temp = temp * 10 + a

print('+'.join(map(str, arr)), '=', c)