# -*- author:caoyue -*-
import os
from urllib import request, parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&fenlei=256&oq=%25E5%258F%25A4%25E5%25A4%25A9%25E4%25B9%2590&rsv_pq=880185280028a9a7&rsv_t=b9a4RvbdlMZtnqt3jKblPwp6i2%2FhHFRmbwrtMgNvwfvYcUFfN3pIGJvoBz8&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=16575&rsv_sug3=25&rsv_sug1=19&rsv_sug7=101&rsv_sug2=0&rsv_sug4=17443&'


# 在请求头加User-Agent，模拟浏览器发送数据
# res = request.urlopen(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

params = {
    'wd': '姚慧'
}

params = parse.urlencode(params)

print(params)

new_url = url + params

print(new_url)

# Request 的方法专门用来加请求头信息
req = request.Request(new_url, headers=headers)

res = request.urlopen(req)

con = res.read().decode()
os.chdir(r'C:\Users\Administrator\Desktop\spider\htmls')
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(con)













