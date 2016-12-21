# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JobItem(scrapy.Item):
    position_id = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    position_name = scrapy.Field()
    position_link = scrapy.Field()

