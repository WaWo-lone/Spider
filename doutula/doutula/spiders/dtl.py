# -*- coding: utf-8 -*-
import os

import scrapy

from doutula.items import DoutulaItem


class DtlSpider(scrapy.Spider):
    name = 'dtl'
    allowed_domains = ['doutula.com']
    start_urls = ['https://www.doutula.com/photo/list/?page=1']

    def parse(self, response):
        # alts = response.xpath('//div[@class="page-content text-center"]//img/@alt').getall()
        srcs = response.xpath('//div[@class="page-content text-center"]//img/@data-original').getall()
        item = DoutulaItem(image_urls=srcs)
        yield item

        next_page_url = response.xpath('//a[@rel="next"]/@href').get()
        next_page = next_page_url.split('=')[-1]

        if int(next_page) < 7:
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse)

    '''自定义方法
    def parse(self, response):
        page = response.url.split('=')[-1]
        alts = response.xpath('//div[@class="page-content text-center"]//img/@alt').getall()
        srcs = response.xpath('//div[@class="page-content text-center"]//img/@data-original').getall()
        for alt, src in zip(alts, srcs):
            item = DoutulaItem(alt=alt, src=src, page=page)
            yield item

        next_page_url = response.xpath('//a[@rel="next"]/@href').get()
        next_page = next_page_url.split('=')[-1]

        if int(next_page) < 7:
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse)
    '''





