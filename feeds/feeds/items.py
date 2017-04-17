# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeedsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SiteItem(scrapy.Item):
    _type = scrapy.Field()
    _group = scrapy.Field()
    rank = scrapy.Field()
    domain = scrapy.Field()
    description = scrapy.Field()
