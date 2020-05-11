# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from unionapp.items import UnionappItem


class WxSpider(CrawlSpider):
    name = 'wx'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        # 列表页
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d+'), follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()
        item = UnionappItem(title=title)
        yield item
