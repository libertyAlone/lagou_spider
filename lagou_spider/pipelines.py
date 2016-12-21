# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.conf import settings
import json
class LagouPipeline(object):
    collection_name = 'hires'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = settings['MONGODB_SERVER'],
            mongo_db = settings['MONGODB_DB']
        )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db.drop_collection(self.collection_name)
    def close_spider(self, spider):
        self.client.close()
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('没有在 %s 中找到 %s ' % (item['url'], data))
        if valid:
            # log.msg('fuck',item)
            self.db[self.collection_name].insert(dict(item))
            log.msg("写入Mongodb %s/%s" %
                    (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
        return item
