# -*- author:caoyue -*-
import json
from urllib import request, parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://movie.douban.com/j/chart/top_list?'

params = {
    'type_name': '爱情',
    'type': 13,
    'interval_id': '100:90',
    'start': 0,
    'limit': 20
}

params_url = parse.urlencode(params)

new_url = url + params_url

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

req = request.Request(new_url, headers=headers)

res = request.urlopen(req)

con = res.read()

print(json.loads(con))



