a = float(input('请输入你的当月利润(万元):'))

rat = (0, 10, 7.5, 5, 3, 1.5, 1)
arr = (0, 10, 20, 40, 60, 100, float('inf'))

b = 0


for i in range(1,len(arr)):
    if a > arr[i]:
        c = (arr[i] - arr[i-1]) * (rat[i] / 100)
        b += c
        print(arr[i], '-', arr[i-1], '万元:', rat[i],'%提成', c, '万元')
    else:
        c = (a - arr[i-1]) * (rat[i] / 100)
        b += c
        print(arr[i], '-', arr[i - 1], '万元:', rat[i],'%提成', c, '万元')
        break

print('奖金合计为(万元):', b)
