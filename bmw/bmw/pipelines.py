# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

class BmwPipeline(object):
    def process_item(self, item, spider):
        return item


class BmwImagesPipeline(ImagesPipeline):

	def get_media_requests(self, item, info):
		request_objs = super(BmwImagesPipeline,self).get_media_requests(item,info)

		for request_obj in request_objs:
			request_obj.item = item
		return request_objs

	def file_path(self, request, response=None, info=None):
		path = super(BmwImagesPipeline,self).file_path(request,response,info)
		path = path.replace('full',request.item.get('title'),1)
		print(path)
		return path