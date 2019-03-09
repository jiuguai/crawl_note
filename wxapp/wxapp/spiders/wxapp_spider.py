# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+list&catid=2&page=\d$'), follow=True),
        Rule(LinkExtractor(allow=r'article-\d+-\d+\.html'),callback="parse_detail",  follow=False),
    )

    def parse_detail(self, response):
        print('='*30)
        print(response.url)

        title = response.xpath('//h1/text()').get()
        authors = response.xpath('//p[@class="authors"]')
        author = authors.xpath('./a/text()').get()
        date = authors.xpath('./span/text()').get()
        article_content = response.xpath('//td[@id="article_content"]').get()

        item = WxappItem(title=title,author=author,date=date,content=article_content)


        yield item
