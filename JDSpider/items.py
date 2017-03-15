# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class JdItemLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    utc_timestamp_in = TakeFirst()


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    product_id = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    gift_id = scrapy.Field()
    merchant = scrapy.Field()
    merchant_grade = scrapy.Field()
    express = scrapy.Field()
    utc_timestamp = scrapy.Field()

