import os
import re

import requests

from settings import *


class YouDaoDownFile:
	def __init__(self, start_url, path='download'):
		"""初始化
		
		跟新url
		
		Arguments:
			start_url {string} -- 起始url
		
		Keyword Arguments:
			path {str} -- 路径默认为当前目录download目录下 (default: {'download'})
		"""
		self.start_url = start_url

		self.path = path
		self.down_len = 0

		patt = r'group/(?P<gid>\d+).+?shareToken=(?P<share_token>\w+)'
		parmas = re.search(patt,self.start_url).groupdict()
		parmas['file_id'] = '{file_id}'
		self.template_url = TEMPLATE_URL.format(**parmas)

		if not os.path.exists(self.path):
			os.makedirs(self.path)

	def start_request(self):
		rep = requests.get(self.start_url,headers=HEADERS)
		self.infos = rep.json()['children']
		self.info_len = len(self.infos)

	def get_urls(self):
		for child in self.infos:
			yield (child['name'],self.template_url.format(file_id=child['fileId']))

	def downloader(self,file_name,donwload_url):
		rep = requests.get(donwload_url,headers=HEADERS)
		with open(os.path.join(self.path,file_name),'wb') as f:
			f.write(rep.content)

	def run(self):
		self.start_request()
		for file_info in self.get_urls():
			self.downloader(*file_info)
			self.down_len += 1
			print('\r已经下载%.2f%%' %(self.down_len*100/self.info_len),end='')


if __name__ == '__main__':
	start_url = 'https://note.youdao.com/yws/api/group/10042410/share?method=get&shareToken=A4EB9037044F4694B41708140F5A9FED'

	path = r"C:\Users\zero\Desktop\bootstrap\animation"
	yddl = YouDaoDownFile(start_url, path)
	yddl.run()
	print()
	
