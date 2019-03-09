# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bmw_crawl.items import BmwCrawlItem
import re
tran_bigpic_url = re.compile('(?<=/)t_')


class BmwFiveSpider(CrawlSpider):
    name = 'bmw_five'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'car.+?pic/series/65-'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath('//div[@class="uibox"]/div[1]/text()').get()
        image_urls = response.xpath('//div[@class="uibox"]/div[2]/ul/li//img/@src').getall()
        image_urls = [tran_bigpic_url.sub('',response.urljoin(image_url)) for image_url in image_urls]

        item = BmwCrawlItem(
            title = title,
            image_urls = image_urls
        )

        yield item

