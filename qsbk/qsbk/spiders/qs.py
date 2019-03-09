# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsSpider(scrapy.Spider):
    name = 'qs'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    def parse(self, response):
    	duanzis = response.xpath('//div[@id="content-left"]/div')

    	for duanzi in duanzis:
    		content = duanzi.xpath('.//div[@class="content"]/span/text()').getall()
    		content = ''.join(map(lambda x:x.strip(),content))
    		author = duanzi.xpath('.//h2/text()').get().strip()
    		item = QsbkItem(author=author,content=content)
    		yield item
    	next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()

    	if next_url:
    		yield scrapy.Request(response.urljoin(next_url),callback =self.parse)
    	else:
    		return