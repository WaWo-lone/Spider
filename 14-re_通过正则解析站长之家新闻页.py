# -*- author:caoyue -*-
import re
import requests

res = requests.get('https://www.chinaz.com/')

con = res.content.decode()

img_urls = re.findall(r'<li.*?class="single-mode">.*?<div class="thumb">.*?<img.*?data-original="(.*?)".*?</div>', con, re.S)

titles = re.findall(r'<li.*?class="single-mode">.*?<h3>\s+<a.*?>(.*?)</a>.*?</h3>', con, re.S)
new_titles = []
for title in titles:
    new_title = re.sub(r'\s+', '', title)
    new_titles.append(new_title)

print(new_titles)

tags = re.findall(r'<div class="tags">.*?([^<>]*?)</a>\s+</div>', con, re.S)
# print(tags)

data = []


for img_url, title, tag in zip(img_urls, new_titles, tags):
    data.append({
        'img_url': img_url,
        'title': title,
        'tag': tag
    })

print(data)