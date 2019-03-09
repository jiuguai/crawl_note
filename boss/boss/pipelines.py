from scrapy.exporters import JsonLinesItemExporter
import pymongo

class BossPipeline:
	def __init__(self,mongo_url,mongo_db,mongo_collection):
		self.mongo_url = mongo_url
		self.mongo_db = mongo_db 
		self.mongo_collection = mongo_collection

	@classmethod
	def from_crawler(cls,crawler):
		return cls(
			mongo_url = crawler.settings.get('MONGO_URL'),
			mongo_db = crawler.settings.get('MONGO_DB'),
			mongo_collection = crawler.settings.get('MONGO_COLLECTION'),
		)

	def open_spider(self,spider):
		self.cli = pymongo.MongoClient(self.mongo_url)
		self.db = self.cli[self.mongo_db]

	def close_spider(self,spider):
		self.cli.close()

	def process_item(self,item,spider):
		self.db[self.mongo_collection].insert(dict(item))
		return item




# class BossPipeline:
# 	def __init__(self):
# 		self.f = open('boss.json','wb')
# 		self.exporter = JsonLinesItemExporter(self.f,ensure_ascii=False,encoding='utf-8')

# 	def process_item(self,item,spider):
# 		self.exporter.export_item(item)

# 		return item

# 	def __del__(self):
# 		self.f.close()

