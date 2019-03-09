import requests
from urllib.parse import urljoin
import random

import os


from pyquery import PyQuery as pq
import re

import pymongo
import json

from settings import *

from concurrent.futures import ThreadPoolExecutor
from threading import Thread,Lock,current_thread
import time


mongo_con = pymongo.MongoClient(**MONGO_CON_DIC)
cs_zf = mongo_con.soufang.cs_zf_new
lock = Lock()

def crawler(url,parse_func,**kwargs):
	count = 0
	try :
		rep = requests.get(url,**kwargs)
		rep.encoding = rep.apparent_encoding
		rep.raise_for_status()
		return parse_func(rep.text)
	except:
		count += 1
		if count < 3: return crawler(url,parse_func,**kwargs)
		return None
	
def parseOneUrl(html):
	doc = pq(html)
	h_infos = doc('.houseList dl')
	for info in h_infos.items():
		title = info('.title a').attr('title')
		path = info('.title a').attr('href')
		house_type = info('.font15.mt12').text()
		addr = info(".gray6.mt12").text()
		detail = info("div[id*=rentid] .mt12").text()
		price = info(".moreInfo").text()
		status = info("dd>.mt12>.note").text()
		status = info("dd>.mt12>.note").text().replace(' ','|')
		
		if not title:continue
		d = {
			"title":title,
			"detail_url": urljoin("http://cs.zu.fang.com" , path),
			"house_type":house_type,
			"address":addr,
			"detail":detail,
			"status":status,
			"price":price
		}
		yield d
	# return len(info)

def saveToMongo(data):
	cs_zf.insert(data)

def concatUrl(count):
	return "http://cs.zu.fang.com/house/i3" + str(count) +"/"

def getUrl():
	for i in range(START_PAGE,MAX_PAGE+1):
		url = concatUrl(i)
		yield url


def crawleCSZU(url,save_func):
	global count
	headers = {}

	headers['User-Agent'] = random.choice(USER_AGENT)

	datas = crawler(url,parse_func=parseOneUrl ,headers=headers,timeout=20)

	if not datas:
		requst_err_urls.append(url)
	for d in datas:
		
		if d:
			save_func(d)
			lock.acquire()
			count += 1
			print(d["title"] ,d["detail_url"])
			print("%s : %s条" %(current_thread().getName(),count))
			print("="*50)
			lock.release()	



count = 0
requst_err_urls = []
gen_url = getUrl()

tpool = ThreadPoolExecutor(max_workers=os.cpu_count()*5)

if __name__ == '__main__':

	start_time = time.time()
	for url in gen_url:
		tpool.submit(crawleCSZU,url,saveToMongo)

	tpool.shutdown()
	mongo_con.close()
	with open('requsts_err_url.json','w',encoding="gbk") as f:
		json.dump(requst_err_urls,f)
	print(requst_err_urls)

	end_time = time.time()

	print('耗时 %.2f' %(end_time - start_time))
	# print(result)

