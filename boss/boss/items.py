# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job = scrapy.Field()
    salary = scrapy.Field()
    demand = scrapy.Field()
    company = scrapy.Field()
    company_digest = scrapy.Field()
    job_detail = scrapy.Field()
    pass
