from scrapy.exceptions import DropItem
import pymysql

class JanShuPipeline:


	def __init__(self):
		self.sql= """
		INSERT INTO jst_pg(title, publish_time, author, content, words_count, page_url, user_home, comments_count, likes_count, views_count,special_id,special) VALUES ( %(title)s, %(publish_time)s, %(author)s, %(content)s, %(words_count)s, %(page_url)s, %(user_home)s, %(comments_count)s, %(likes_count)s, %(views_count)s,%(special_id)s,%(special)s);
		"""
		self.con = pymysql.connect(host='localhost',user="root",password="root",database='jianshu',port=3306)
	def open_spider(self,spider):
		
		self.cursor = self.con.cursor()


	def process_item(self,item,spider):
		
		try:
			self.cursor.execute(self.sql,dict(item))
			self.con.commit()
		except Exception as e:
			print('='*30,'出错了')
			print(item['page_url'])
			print(e)
			raise DropItem(item['page_url'])
		return item

	def close_spider(self,spider):
		self.con.close()


