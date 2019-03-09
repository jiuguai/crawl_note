from urllib import request,parse
import re
from lxml import etree
import requests
import pymysql
from threading import Thread,Lock,currentThread,active_count
import json
import random
from settings import *
from soufang_logger import getLogger
import pymongo


logger = getLogger()
lock = Lock()
User_Agent = USER_AGENT


class SouFang:
    def __init__(self):
        # self.data = []
        self.city_url = []

        if DB_TYPE == "MySQL":
            self.mysql_con = pymysql.connect(MYSQL_CON_INFO)
            self.insert_SQL = MSQL_INSET_STR
            self.cursor = self.mysql_con.cursor()
        if DB_TYPE == "mongoDB":
            self.mongo_con = pymongo.MongoClient(**MONGO_CON)
            self.col = self.mongo_con.soufang.new_house


        self.new_count = 0
        
        self._crawl_url()

    def __del__(self):
        if DB_TYPE == "MySQL":
            self.mysql_con.close()
        else:
            self.mongo_con.close()


    # 获取所需要爬取的url
    def _crawl_url(self):
        url = "http://www.fang.com/SoufunFamily.htm"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
        req = request.Request(url,headers=headers)
        rsp = request.urlopen(req)
        txt = rsp.read().decode('gbk')

        patt_citys = """id="sffamily_B03_\d\d".+?</tr>"""
        citys = re.findall(patt_citys,txt,re.S)

        patt_city = """<a href="(.+?)".+?>(.+?)</a>"""
        patt_province = "<strong>(.+?)</strong>"
        i = 0
        for city in citys:
            ct = re.findall(patt_city,city,re.S)
            pro = re.search(patt_province,city)
            if pro and pro.group(1) != '&nbsp;': province = pro.group(1)
            if province == '其它':continue
            
            for url,c in ct:
                t = url.split('.',1)
                d = {"province":province,"city":c,"url":url,
                    "new_url":".".join([t[0],"newhouse",t[1]+"house/s/"]),
                    "esf_url":".".join([t[0],"esf",t[1]]),
                     "zu_url":".".join([t[0],"zu",t[1]])
                    }
                self.city_url.append(d)


        # print(len(self.city_url))
        # print(self.city_url)
        self.city_url[0]["new_url"] = 'http://newhouse.fang.com/house/s/'
        self.city_url[0]["esf_url"] = 'http://esf.fang.com'
        self.city_url[0]["zu_url"] = 'http://zu.fang.com'
    
    def parseNewHouse(self):
        # self.city_url = [ {"province":" 云南","city":"文山","url":'http://wenshan.fang.com/',
        #             "new_url":"http://wenshan.newhouse.fang.com/house/s/",
        #             }]

        for i in range(10):
            Thread(target=self.__parseNewHouse).start()


    def __parseNewHouse(self):
        while True:
            if not len(self.city_url): return
            data = self.city_url.pop()
  
            url = data['new_url']
            i = 1
            while True:
                _url = '%sb9%i/' %(url,i)
                headers = {"User-Agent":random.choice(User_Agent)}
                try:
                    rep = requests.get(_url,headers= headers)
                except :
                    logger.error('请求异常 - %s %s' %(data['city'],_url))
                i += 1
                try:
                    txt = rep.text.encode("latin1").decode("gbk")
                except:
                    logger.error('编码解析异常 - %s %s' %(data['city'],_url))
                ht = etree.HTML(txt)
                elements = ht.xpath("//div[@id='newhouse_loupai_list']/ul/li")
                if not elements: break
                for e in elements:
                    self._parseNewHouse(e,data,_url)

    def save_to_mysql(self,data):
        self.cursor.execute(self.insert_SQL,data)
        self.mysql_con.commit()

    def save_to_mongo(self,data):
        self.col.insert(data)

    def _parseNewHouse(self,e,data,crawle_url):
        try:
            name = e.xpath(".//div[@class='nlcd_name']/a/text()")
            if not name: return
            name = name[0].strip() if name else ""
            if not name: return
            print(currentThread().getName(),data['city'],name)

            sale = re.sub('(?:\s|广告)','',''.join(e.xpath(".//div[@class = 'nhouse_price']//text()")))
            if not sale: 
                sale = e.xpath('.//div[@class="kanzx"]/h3//text()')
                sale = sale[0].strip() if sale else ""
                if sale == "优惠楼盘":
                    t = data['url'].split('.',1)
                    self.city_url.append({"province":data["province"],"city":data["city"],
                         "new_url":".".join([t[0],"newhouse",t[1]+"house/dianshang/"]).replace("bj.",""),
                    })
                    return

            rooms = e.xpath(".//div[@class='house_type clearfix']/a/text()")
            rooms = list(filter(lambda x:re.match('\d居',x),rooms))
            rooms = re.sub('\s','','/'.join(rooms))

            area = e.xpath(".//div[@class='house_type clearfix']/text()")
            area = ''.join(area)
            area = re.search('\d+?(?:~\d+)?平米',area)
            area = area.group() if area else ""

            addr = e.xpath(".//div[@class='address']/a/@title")
            addr = addr[0] if addr else ""
            
            district = ''.join(e.xpath(".//div[@class='address']/a//text()"))
            district = re.search('\[([^\]]+?)\]',district)
            district = district.group(1) if district else ""

            sale_state = e.xpath(".//div[contains(@class,'fangyuan')]/span/text()")
            sale_state = sale_state[0] if sale_state else ""

            house_type = '/'.join(e.xpath(".//div[contains(@class,'fangyuan')]/a/text()"))

            
            origin_url = e.xpath(".//div[@class='nlcd_name']/a/@href")
            patt = 'https?://(?!adshow).+?$'
            origin_url = re.search(patt,origin_url[0]).group() if origin_url else ""


            # self.data.append({"name":name,"rooms":rooms,"area":area,"addr":addr,"district":district,"sale_state":sale_state,
            #          "house_type":house_type,"sale":sale,"origin_url":origin_url
            #          })
        except:
            logger.error('数据解析异常 - %s %s :%s' %(data['city'],name,crawle_url))
            return

        try:
            
            if DB_TYPE == "MySQL":
                lock.acquire()
                self.save_to_mysql((
                data["city"],data["province"],name,rooms,area,addr,district,sale_state,house_type,sale,origin_url
                ))
                lock.release()
            else:
                self.save_to_mongo({'city':data['city'],'lp_name':name})
            
            self.new_count += 1
            print("%i条" %self.new_count)
            
            
            print('='*20)
        except Exception as e:
            if DB_TYPE == "MySQL": lock.release()
            logger.error('数据存储异常 - %s %s :%s %s' %(data['city'],name,crawle_url,e))

    
sf = SouFang()
# print(len(sf.city_url))
# print(sf.city_url)
# x = list(filter(lambda x:x["province"] == '&nbsp;',sf.city_url))
# print(len(x))
# print(x)

sf.parseNewHouse()