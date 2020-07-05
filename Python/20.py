# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

h = 100

arr = []

temp = h
for i in range(10):
    temp /= 2
    arr.append(temp)

print(arr)
print('共经过:', 3 * sum(arr) - arr[-1])
print('第十次：', arr[-1])
