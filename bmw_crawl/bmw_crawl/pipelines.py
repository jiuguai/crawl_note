# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

class BmwCrawlPipeline(ImagesPipeline):

	def get_media_requests(self, item, info):
		request_objs = super(BmwCrawlPipeline,self).get_media_requests( item, info)
		for obj in request_objs:
			obj.item = item
		return request_objs

	def file_path(self, request, response=None, info=None):
		path = super(BmwCrawlPipeline,self).file_path(request, response, info)

		path = path.replace('full',request.item.get('title'),1)

		return path