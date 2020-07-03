# 模拟Linux用户登录。
#
# 验证账号和密码，若失败则延迟三秒输出错误信息。

import time

global user, name

user = {
    'pipilugao': '1234',
}


def login():
    global name
    name = input('Username:')
    pswd = input('Password:')
    if name not in user:
        return False
    return user[name] == pswd


while (not login()):
    time.sleep(3)  # 暂停3秒
    print('Authentication failure')

print(name + '@localhost:~$')
