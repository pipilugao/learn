# 格式化输出当前时间。
#
# 使用 time 模块，格式为 yyyy-mm-dd HH:mm:ss。

import time

a = time.localtime()

b = time.strftime('%Y-%m-%d %H:%M:%S', a)
print(b)
