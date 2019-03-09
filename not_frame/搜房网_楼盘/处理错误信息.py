import re
import requests
from pyquery import PyQuery as pq
import pymysql
with open('err.log','r',encoding='utf-8') as f:
	s = f.read()
	f.close()


patt = '([^\s]+?异常) - ([^s]+) ([^s]+) ([^ :]+) :(.+)'
l = re.findall(patt,s)

# print(len(l))
# print(l)
key = ("exception_type","province","city","lp_name","crawle_url")
e_l = map(lambda x:dict(zip(key,x)),l)
# e_l = list(e_l)

# print(e_l)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}

# # ,city,lp_name
def get_url(url):
	rep = requests.get(url,headers=headers)
	return rep.text.encode('latin1').decode('gbk')

insert_SQL = """
            INSERT INTO new_house(
            city ,province ,lp_name ,rooms ,area ,addr ,district ,sale_state ,house_type ,sale,origin_url
            ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """


def parse_url(data,d):


	doc = pq(data)
	li = doc('.nhouse_list #newhouse_loupai_list li:contains('+d['lp_name']+')')
	lp_name = li('.nlcd_name').text()
	sale = li('.nhouse_price').text()
	rooms = li('.house_type a').text().replace(' ','/')
	area = re.search('(?<=－ )\d.+',li('.house_type').text())
	area = area.group() if area else ''
	addr = li('.address a').attr('title')
	district = re.search('(?<=\[).+?(?=\])',li('.address a').text())
	district = district.group() if district else ""
	sale_state = li('.fangyuan span').text()
	house_type = li('.fangyuan a').text().replace(' ','/')
	origin_url = re.search('https?://(?!adshow).+?$',li('.nlcd_name a').attr('href')).group()


	return (d['city'],d['province'],lp_name,rooms,area,addr,district,sale_state,house_type,sale,origin_url)

mysql_con = pymysql.connect(
            host="localhost",user="root",
            password="root",database="soufang",
            port=3306,
        )
cur = mysql_con.cursor()

err_l = []
# data_l = []
for d in e_l:
	try :
		html = get_url(d['crawle_url'])
		data = parse_url(html,d)

		cur.execute(insert_SQL,data)
		mysql_con.commit()
		print(data)
	except:
		err_l.append(d)


# print(data_l)
print("="*50)
print(err_l)
# cur.close()
# url = 'http://honghe.newhouse.fang.com/house/s/b91/'
# data = get_url(url)
# t = parse_url(data)
# print(t)

# print(s)
