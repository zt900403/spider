import scrapy
import re
from scrapy.loader import ItemLoader
from JDSpider.items import JdspiderItem, JdItemLoader
from datetime import datetime
import json

class JDSpider(scrapy.Spider):
    name = 'JDSpider'

    start_urls = [
        #'http://www.jd.com'
        'https://item.jd.com/4245882.html',
        'https://item.jd.com/3878237.html?cpdad=1DLSUE'
    ]

    id_regex = re.compile(r'(\d+).html')

    def get_product_id(self, url):
        result = self.id_regex.search(url)
        if result:
            return result.group(1)
        else:
            return None

    def parse(self, response):
        product_id = self.get_product_id(response.url)
        if product_id:
            j = JdItemLoader(item=JdspiderItem(), response=response)
            j.add_xpath('name', '//div[@id="crumb-wrap"]//div[@class="item ellipsis"]/text()')
            j.add_xpath('title', '//div[@class="w"]/div[@class="product-intro clearfix"]//div[@class="sku-name"]/text()')
            j.add_value('product_id', product_id)
            j.add_value('utc_timestamp', int(datetime.utcnow().timestamp()))
            item = j.load_item()
            request = scrapy.Request('https://p.3.cn/prices/mgets?skuIds=J_' + str(product_id),
                                    callback=self.parse_page2)
            request.meta['item'] = item
            yield request

    def parse_page2(self, response):
        item = response.meta['item']
        print(item)
        print(json.loads(response.body_as_unicode())[0]['p'])
        yield item
