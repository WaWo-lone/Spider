# -*- author:caoyue -*-
import time
from threading import Thread
from urllib import request

import requests
from lxml import etree
from queue import Queue
import os

start_time = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Referer': 'https://www.doutula.com/photo/list/'
}
base_dir = os.path.join(os.path.join(os.getcwd(), 'images'), 'doutula')
url_queue = Queue()
img_queue = Queue()

def parse_url():
    while True:
        if url_queue.empty():
            break

        url, page = url_queue.get()
        res = requests.get(url, headers=headers)

        # 返回的响应码错误，爬取失败，继续爬取
        if res.status_code == 520:
            continue

        con = res.text
        html = etree.HTML(con)
        srcs = html.xpath('//div[@class="page-content text-center"]//img/@data-original')
        alts = html.xpath('//div[@class="page-content text-center"]//img/@alt')

        page_path = os.path.join(base_dir, str(page))
        if not os.path.exists(page_path):
            os.mkdir(page_path)

        for src, alt in zip(srcs, alts):
            img_name = alt + os.path.splitext(src)[1]
            img_path = os.path.join(page_path, img_name)
            img_queue.put((src, img_path))


def download_img():
    while True:
        if img_queue.empty() and url_queue.empty():
            break

        try:
            src, img_path = img_queue.get()
            request.urlretrieve(src, img_path)
        except:
            continue


if __name__ == '__main__':
    for i in range(1, 7):
        url = 'https://www.doutula.com/photo/list/?page=%s' % i
        url_queue.put((url, i))

    ts = []
    # 创建请求资源的线程
    for x in range(3):
        t = Thread(target=parse_url)
        ts.append(t)

    # 创建下载图片的线程
    for y in range(3):
        t = Thread(target=download_img)
        ts.append(t)

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    print(time.time() - start_time)








