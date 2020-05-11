# -*- author:caoyue -*-
import base64
import json
import urllib.request
from urllib import parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def getcode():
    #修改API说明修改接口地址
    host = 'https://imgurlocr.market.alicloudapi.com'
    path = '/urlimages'
    method = 'POST'
    appcode = 'fa6781aae5104bdf827cc93c9afaff85'
    querys = ''
    bodys = {}
    url = host + path

    # 组装本地需要识别的图片
    fp = open('./code.jpg', 'rb')
    res = base64.b64encode(fp.read()).decode()
    bodys['image'] = 'data:image/jpeg;base64,' + res

    post_data = urllib.parse.urlencode(bodys).encode(encoding='UTF8')
    request = urllib.request.Request(url, post_data)
    #根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    request.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)

    content = response.read()
    if (content):
        res = json.loads(content.decode('UTF-8'))
        code = res['result'][0]['words']
        return code

if __name__ == '__main__':
    code = getcode()
    print(code)