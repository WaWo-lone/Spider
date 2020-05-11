# -*- author:caoyue -*-
import os
from urllib import request, parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
os.chdir(r'C:\Users\Administrator\Desktop\spider\htmls')
for i in range(1, 3):
    pn = (i - 1) * 50
    params = {
        'kw': 'lol',
        'pn': pn
    }
    params_url = parse.urlencode(params)
    url = 'https://tieba.baidu.com/f?' + params_url
    req = request.Request(url, headers=headers)
    res = request.urlopen(req)
    con = res.read()
    with open(f'lol_{i}.html', 'wb') as f:
        f.write(con)
