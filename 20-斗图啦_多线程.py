# -*- author:caoyue -*-
import time

import requests
import os
from lxml import etree
from urllib import request
from threading import Thread

start_time = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Referer': 'https://www.doutula.com/photo/list/'
}

base_dir = os.path.join(os.path.join(os.getcwd(), 'images'), 'doutula')

def download(url, page):

    res = requests.get(url, headers=headers)

    con = res.text

    html = etree.HTML(con)

    srcs = html.xpath('//div[@class="page-content text-center"]//img/@data-original')
    alts = html.xpath('//div[@class="page-content text-center"]//img/@alt')

    # print(srcs)

    page_path = os.path.join(base_dir, str(page))
    if not os.path.exists(page_path):
        os.mkdir(page_path)

    # opener = request.build_opener()
    # opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36")]
    # request.install_opener(opener)

    for src, alt in zip(srcs, alts):
        img_name = alt + os.path.splitext(src)[1]
        img_path = os.path.join(page_path, img_name)
        # print(img_path)
        try:
            request.urlretrieve(src, img_path)
        except:
            continue

def run(i):
    start = 2*i+1
    end = 2*i+3
    for n in range(start, end):
        url = f'https://www.doutula.com/photo/list/?page={n}'
        download(url, n)

ts = []
for i in range(0, 3):
    t = Thread(target=run, args=(i,))
    ts.append(t)

for t in ts:
    t.start()

for t in ts:
    t.join()

print(time.time()-start_time)




