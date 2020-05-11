# -*- author:caoyue -*-
import os

import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# verify参数设置为False，则不会判断ssl证书是否安全
req = requests.get('https://www.shaileba.com/', verify=False)

con = req.content

os.chdir(r'C:\Users\Administrator\Desktop\spider\htmls')
with open('shaileba.html', 'wb') as f:
    f.write(con)