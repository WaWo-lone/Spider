# -*- author:caoyue -*-
import os

import requests
from lxml import etree
from urllib import request

url = 'http://sc.chinaz.com/tupian/meinvtupian.html'

res = requests.get(url)

con = res.content.decode()

html = etree.HTML(con)

alts = html.xpath('//div[@id="container"]//img/@alt')
img_urls = html.xpath('//div[@id="container"]//img/@src2')
# print(img_urls)
for alt, img_url in zip(alts, img_urls):
    img_name = alt + os.path.splitext(img_url)[1]
    request.urlretrieve(img_url, './images/girls/' + img_name)





