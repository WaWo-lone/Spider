# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request

from scrapy.pipelines.images import ImagesPipeline

from doutula.settings import IMAGES_STORE


class DoutulaPipeline:
    def __init__(self):
        self.images_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

    def process_item(self, item, spider):
        page_path = os.path.join(self.images_dir, item.get('page'))
        if not os.path.exists(page_path):
            os.mkdir(page_path)
        image_name = item.get('alt') + os.path.splitext(item.get('src'))[1]
        request.urlretrieve(item.get('src'), os.path.join(page_path, image_name))
        return item

# 自定义 pipeline 类，要继承 ImagesPipeline
class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requests = super().get_media_requests(item, info)
        for index, request in enumerate(requests):
            request.page = item.get('page')
            request.alt = item.get('alts')[index]
        return requests

    def file_path(self, request, response=None, info=None):
        page = request.page
        page_path = os.path.join(IMAGES_STORE, page)
        if not os.path.exists(page_path):
            os.mkdir(page_path)

        image_name = request.alt + os.path.splitext(request.url)[1]

        return f'{page}/{image_name}'

