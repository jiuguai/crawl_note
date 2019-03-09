import scrapy
import json

class UseragentSpider(scrapy.Spider):
    name = 'useragent'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/user-agent']

    def parse(self, response):
    	result = json.loads(response.text)
    	print('='*30)
    	
    	print(result)
    	yield scrapy.Request(self.start_urls[0],dont_filter=True)