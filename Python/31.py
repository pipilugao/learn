# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

a = input('请输入第一个字母：')
b = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
if a.upper() == 'M':
    print(b[0])
elif a.upper() == 'T':
    a = input('请输入第二个字母：')
    if a.upper() == 'U':
        print(b[1])
    elif a.upper() == 'H':
        print(b[3])
    else:
        print('第二个字母输入不正确')
elif a.upper() == 'W':
    print(b[2])
elif a.upper() == 'F':
    print(b[4])
elif a.upper() == 'S':
    a = input('请输入第二个字母：')
    if a.upper() == 'A':
        print(b[5])
    elif a.upper() == 'U':
        print(b[6])
    else:
        print('第二个字母输入不正确')
else:
    print('第二个字母输入不正确')