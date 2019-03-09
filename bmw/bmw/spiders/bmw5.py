# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem
import re

tran_bigurl = re.compile('(?<=/)t_')

class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['autohome.com']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')
        for uibox in uiboxs:
        	title = uibox.xpath('./div[@class="uibox-title"]/a/text()').get()
        	img_urls = uibox.xpath('.//ul/li[position()<last()]//img/@src').getall()

        	img_urls = [tran_bigurl.sub('',response.urljoin( umg_url)) for umg_url in img_urls]

        	item = BmwItem(
        			title=title,
        			image_urls = img_urls
        		)
        	yield item


