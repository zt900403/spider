# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    gift_id = scrapy.Field()
    merchant = scrapy.Field()
    date = scrapy.Field()

