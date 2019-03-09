# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MiddlewarePipeline(object):
	def __init__(self):
		# 建立连接

		# SQL 语句
		self.sql= """
		INSERT INTO jst_pg(title, publish_time, author, content, words_count, page_url, user_profiel, comments_count, likes_count, views_count,special_id) VALUES ( %(title)s, %(publish_time)s, %(author)s, %(content)s, %(words_count)s, %(page_url)s, %(user_profiel)s, %(comments_count)s, %(likes_count)s, %(views_count)s,%(special_id)s);
		"""
		self.con = pymysql.connect(host='localhost',user="root",password="root",database='jianshu',port=3306)


	def open_spider(self,spider):
		# 创建游标
		self.cursor = slef.con.cursor()
		pass

    def process_item(self, item, spider):
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
    	pass
