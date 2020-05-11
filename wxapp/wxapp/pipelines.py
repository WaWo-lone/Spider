# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class WxappPipeline:
    # 爬虫开启时，执行的方法。等同于 __init__
    def open_spider(self, spider):
        self.fp = open('wxapp.txt', 'ab')
        # 实例化exporter
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def process_item(self, item, spider):
        # 写入数据
        self.exporter.export_item(item)
        return item

    # 爬虫结束时，执行的方法，等同于 __del__
    def close_spider(self, spider):
        self.fp.close()
