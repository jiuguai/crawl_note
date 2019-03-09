from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline(object):
	def open_spider(self,spider):
		self.fp = open('qs.json','wb')
		self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
	def process_item(self,item,spider):
		self.exporter.export_item(item)
		print(item)
		return item
	def close_spider(self,spider):
		
		self.fp.close()




