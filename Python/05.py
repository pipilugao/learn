# 输入三个整数x,y,z，请把这三个数由小到大输出。


a = input('请输入三个整数（x-x-x）：')

while a.count('-') != 2:
    a = input('请重新输入三个整数（x-x-x）：')

arr = a.split('-')
res = max(arr)
print('max:', res)
