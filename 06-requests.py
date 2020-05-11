# -*- author:caoyue -*-
import requests

# 使用get方法请求资源
req = requests.get(url='https://www.baidu.com/')

# 返回数据
# 1、通过text属性，会自动解析数据的编码格式
# 返回结果，如果是中文，可能会解析错误，出现乱码

# 如果出现乱码，可以设置编码
req.encoding = 'utf-8'

# res = req.text

# 2、content通过字节的形式返回数据
res = req.content.decode()

print(res)
