# -*- coding: utf-8 -*-
import scrapy
import json

class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/ip']

    def parse(self, response):
    	# result = json.loads(response.text)
    	# print('='*30)
    	# print(result)

    	x = response.request.headers
    	print(x)
    	yield scrapy.Request(self.start_urls[0],dont_filter=True)