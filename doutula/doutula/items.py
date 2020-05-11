# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoutulaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    '''自定义
    alt = scrapy.Field()
    src = scrapy.Field()
    page = scrapy.Field()
    '''

    # 内置
    image_urls = scrapy.Field()
    images = scrapy.Field()
