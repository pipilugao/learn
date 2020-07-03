# 输出 9*9 乘法口诀表。

for row in range(1, 10):
    for col in range(1, row + 1):
        print(row, '*', col, '=', row*col, sep='', end='\t')

    print()