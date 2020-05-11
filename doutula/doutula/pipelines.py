# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request


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
