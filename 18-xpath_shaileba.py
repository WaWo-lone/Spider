# -*- author:caoyue -*-
import requests
import os
from lxml import etree
from urllib import request

res = requests.get('https://www.shaileba.com/')

con = res.text

html = etree.HTML(con)

img_urls = html.xpath('//div[@id="girlList"]//img/@src')
names = html.xpath('//div[@id="girlList"]//p/text()')
for img_url, name in zip(img_urls, names):
    img_name = name + os.path.splitext(img_url)[1]
    request.urlretrieve('https://www.shaileba.com/' + img_url, './images/girlList/' + img_name)
