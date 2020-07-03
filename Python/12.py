# 判断101-200之间有多少个素数，并输出所有素数。
#
# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

flag = 0
arr = []

for i in range(101,201):
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        arr.append(i)
    else:
        flag = 0

print('101-200间的素数共计：', len(arr))
print(arr)