# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101250100/?query=python&page=1']

    rules = (
        # Rule(LinkExtractor(allow=r'/c101250100/\?query=python&page=2'), follow=True),
        Rule(LinkExtractor(allow=r'/job_detail/',restrict_xpaths='//div[@class="job-list"]'), callback='parse_detail'),
    )

    def parse_detail(self, response):
        primary_info = response.xpath('//div[@class="job-banner"]//div[@class="info-primary"]')
        company_info = response.xpath('//div[@class="info-company"]')

        item = BossItem()

        item['job'] = primary_info.xpath('.//h1/text()').get()
        item['salary'] = primary_info.xpath('.//span[@class="badge"]//text()').get().strip()

        demand = primary_info.xpath('./p/text()').getall()
        item['demand'] = ' | '.join(demand)
        item['company'] = company_info.xpath('./h3/a/text()').get()

        company_digest = company_info.xpath('./p//text()').getall()
        item['company_digest'] = ' | '.join(company_digest)

        job_detail = response.xpath('//div[@class="detail-content"]/div[1]/div/text()').getall()
        item['job_detail'] = '\n'.join(map(lambda x:x.strip(' \t\n\r\x0c'),job_detail)) 

        yield item

