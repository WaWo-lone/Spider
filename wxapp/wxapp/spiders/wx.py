# -*- coding: utf-8 -*-
import json

import scrapy
from wxapp.items import WxappItem



class WxSpider(scrapy.Spider):
    name = 'wx'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2']
    '''
    def parse(self, response):
        titles = response.xpath('//h3[@class="list_title"]/a/text()').getall()
        srcs = response.xpath('//div[@class="mbox_list recommend_article_list cl"]//img/@src').getall()
        for title, src in zip(titles, srcs):
            item = WxappItem(title=title, src=src)
            yield item

        next_page = response.xpath('//a[@class="nxt"]/@href').get()
        page = next_page[-1]
        if int(page) > 3:
            return
        else:
            yield scrapy.Request(next_page, callback=self.parse)
    '''

    # 直接请求post数据，重写start_requests方法
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        formdata = {
            'kw': 'job'
        }
        yield scrapy.FormRequest(url, formdata=formdata, callback=self.parse_post)

    def parse_post(self, response):
        con = json.loads(response.text)
        print(con)


