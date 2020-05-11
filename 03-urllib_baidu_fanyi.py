# -*- author:caoyue -*-
import json
from urllib import request, parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

# post 方式需要加上提交的数据,需要将数据转为字节形式
data = {
    'kw': 'job'
}
data = parse.urlencode(data).encode()

req = request.Request(url, data=data, headers=headers)

res = request.urlopen(req)

con = res.read()

print(con)

print(json.loads(con))

