import re
import json

import requests 
from lxml import etree

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
url = 'https://www.bilibili.com/video/av24702867/?p=336'

rep = requests.get(url,headers=headers)
text = rep.text

et = etree.HTML(text)
play_data = et.xpath('//script[not(@src) and not(@type)]//text()')[1]
# print(play_data)
patt = r',"pages":(\[.+?\])'
data = re.search(patt,play_data).group(1)

data = json.loads(data)

# print(data)

section_num = 1

sections = {'section':1,'pages':[],'start_page':1,'end_page':None}
dis_data = []
sd = []
start_page = 1
end_page = 1

for d in data:
	if d['part'].startswith('01') and sd:
		# 存储
		sections['pages'] = sd
		sections['end_page'] = d['page'] - 1
		dis_data.append(sections)

		# 重新调整
		section_num += 1
		sections = {'section':section_num,'pages':[],'start_page':d['page'],'end_page':None}
		sd = []
	sd.append(d['part'])
else:
	sections['end_page'] = d['page']
	sections['pages'] = sd
	dis_data.append(sections)
data = json.dumps(dis_data,indent=4,ensure_ascii=False)
print(data)
