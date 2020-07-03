# 输入某年某月某日，判断这一天是这一年的第几天？
#
# 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天。
# 输入格式：yyyy-MM-dd

a = input('请输入日期（yyyy-MM-dd）：')

while a.count('-') != 2:
    a = input('请重新输入日期（yyyy-MM-dd）：')

data = a.split('-')
year = int(data[0])
month = int(data[1])
day = int(data[2])

arr = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

flag = 0

count = 0

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    flag = 1

for i in range(1, 13):
    if month > i:
        temp = arr[i-1]

        if i == 2:
            temp += flag

        count += temp
        print(i, '月：', temp)
    else:
        count += day
        print(month, '月：', day)
        break

print('count:', count)