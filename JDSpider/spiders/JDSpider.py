import scrapy
import re
from scrapy.loader import ItemLoader
from JDSpider.items import JdspiderItem


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
        print(product_id)
        if product_id:
            print('haha')
            p = ItemLoader(item=JdspiderItem(), response=response)
            p.add_xpath('name', '//div[@id="crumb-wrap"]//div[@class="item ellipsis"]/text()')
            p.add_css('title', 'div.sku-name::text')#'//div[@class="itemInfo-wrap"]/div[@class="sku-name"]/text()')
            p.add_value('product_id', product_id)
            a = p.load_item()
            print(a)
