# -*- author:caoyue -*-
import requests
import os
from lxml import etree
from urllib import request

res = requests.get('http://www.tbqq.net/')
con = res.text

html = etree.HTML(con)

srcs = html.xpath('//form[@id="moderate"]//img/@src')
names = html.xpath('//form[@id="moderate"]//div[@class="deanmadouname"]//text()')

for src, name in zip(srcs, names):
    req = requests.get('http://www.tbqq.net/' + src)
    url = req.url
    img_name = name + os.path.splitext(url)[1]
    request.urlretrieve(url, './images/models/' + img_name)
