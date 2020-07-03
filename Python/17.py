# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#
# 利用while语句,条件为输入的字符不为'\n'。

a = input('请输入一行字符:')

count = {'letter': 0, 'space': 0, 'number': 0, 'other': 0}

for i in a:
    if i.isalpha():
        count['letter'] += 1
    elif i.isspace():
        count['space'] += 1
    elif i.isdigit():
        count['number'] += 1
    else:
        count['other'] += 1

print(count)
