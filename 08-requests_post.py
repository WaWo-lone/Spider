# -*- author:caoyue -*-
import json

import requests

data = {
    'kw': 'job'
}

res = requests.post('https://fanyi.baidu.com/sug', data=data)

con = res.content.decode()

print(json.loads(con))
