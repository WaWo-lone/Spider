# -*- author:caoyue -*-
import os
from urllib import request
import ssl

# 如果网站的协议是https的话，加上这个
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'

}
url = 'https://www.chinaz.com/'

req = request.Request(url, headers=headers)

res = request.urlopen(req)

# read 读取整个网页的内容，read获取的数据是二进制的
con = res.read().decode()

os.chdir(r'C:\Users\Administrator\Desktop\spider\htmls')
with open('chinaz.html', 'w', encoding='utf-8') as f:
    f.write(con)

# readline 读取一行数据
# con = res.readline()

# readlines 把每一行数据封装在一个列表里
# con = res.readlines()
# print(con)

# 返回数据的响应状态
# status = res.code  # 200
# status = res.getcode()  # 200
status = res.status  # 200
# print(status)

# 返回请求的url
# url = res.geturl()
# print(url)

# 返回响应头信息
# meta = res.headers
# meta = res.getheaders()  # 列表包元祖形式
# meta = res.info()
# print(meta)

# 保存图片
url = 'https://pic.chinaz.com/thumb/2020/0504/2020050410095647.png'
os.chdir(r'C:\Users\Administrator\Desktop\spider\images')
request.urlretrieve(url, 'chinaz.png')

