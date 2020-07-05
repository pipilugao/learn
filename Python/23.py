# 利用循环打印菱形
#
# 先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列

SIZE = 5
SHOW = ' *'
HIDE = '  '

# 坐标系构建法,线性规划
for y in range(SIZE - 1, -SIZE, -1):
    for x in range(-SIZE + 1, SIZE, 1):
        if (y > x - SIZE) and (y < x + SIZE) and \
                (y > -x - SIZE) and (y < -x + SIZE):
            print(SHOW, end='')
        else:
            print(HIDE, end='')
    print()