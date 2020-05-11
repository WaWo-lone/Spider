# -*- author:caoyue -*-
import requests

proxy = {
    'http': '106.87.84.147:4237'
}

req = requests.get('http://httpbin.org/ip', proxies=proxy)

con = req.content.decode()

print(con)

