# -*- author:caoyue -*-
import os
import re

import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
# res = requests.get('https://www.ygdy8.net/html/gndy/china/index.html', headers=headers)
#
# res.encoding = 'gb2312'
#
# con = res.text
#
# html = etree.HTML(con)
#
# links = html.xpath('//div[@class="co_content8"]//b/a[2]/@href')

def parse_detail(url):
    req = requests.get(url, headers=headers)
    req.encoding = 'gb2312'
    con = req.text
    html = etree.HTML(con)
    img_url = html.xpath('//div[@id="Zoom"]//img[1]/@src')[0]
    content = html.xpath('//div[@id="Zoom"]//p[1]/text()')
    # print(content)
    # 方法一：
    # content = ''.join(content)
    # res = re.search(r'◎片\u3000\u3000名(.*?)◎年\u3000\u3000代(.*?)◎产\u3000\u3000地.*?◎主\u3000\u3000演(.*?)◎标\u3000\u3000签', content)
    # name = res.group(1).strip()
    # year = res.group(2).strip()
    # actors = re.sub(r'\s{2,}', ',', res.group(3)).strip()
    # print(name, year, actors)

    # 方法二：
    name = ''
    year = ''
    actors = []
    for index,con in enumerate(content):
        if con.startswith('◎片\u3000\u3000名'):
            name = con.replace('◎片\u3000\u3000名', '').strip()
        if con.startswith('◎年\u3000\u3000代'):
            year = con.replace('◎年\u3000\u3000代', '').strip()
        if con.startswith('◎主\u3000\u3000演'):
            actor = con.replace('◎主\u3000\u3000演', '').strip()
            actors.append(actor)
            for i in range(index, len(content)):
                if content[i].startswith('◎标\u3000\u3000签') or content[i].startswith('◎简\u3000\u3000介'):
                    break
                act = content[i].strip()
                actors.append(act)
            data.append({
                'img': img_url,
                'name': name,
                'year': year,
                'actors': actors
            })



# urls = []
# for link in links:
#     url = 'https://www.ygdy8.net' + link
#     urls.append(url)
#     parse_detail(url)

with open('movie_urls.txt', 'r') as f:
    res = f.read()

urls = eval(res)

data = []
for url in urls:
    parse_detail(url)


for d in data:
    print(d)