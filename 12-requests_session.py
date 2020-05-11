# -*- author:caoyue -*-
import os

import requests

# 创建一个session对象
session = requests.session()

data = {
    'email': '290793992zb@163.com',
    'password': 'python123'
}

# session 会保存用户登录成功之后的cookie数据
session.post('http://cn.hoyoyo.com/member~login.html', data=data)

res = session.get('http://cn.hoyoyo.com/my_account~profile.html')

con = res.content

os.chdir(r'C:\Users\Administrator\Desktop\spider\htmls')

with open('hoyoyo_mine.html', 'wb') as f:
    f.write(con)

