# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
class RrSpiderSpider(scrapy.Spider):
    name = 'rr_spider'
    allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/PLogin.do']
    start_urls = ['http://zhibo.renren.com']
    def start_requests(self):
      for url in self.start_urls:
          yield scrapy.Request( url,dont_filter=True,callback=self.parse,

            cookies ={'anonymid': 'jnvuek00-d8kdos', ' _ga': 'GA1.3.1571025196.1540910644', ' _gid': 'GA1.3.171189287.1540910644', ' ln_uact': '18774979616', ' ln_hurl': 'http://head.xiaonei.com/photos/0/0/men_main.gif', ' depovince': 'HUN', ' _r01_': '1', ' UM_distinctid': '166c5a9f8ba100-09c5cc6d024b2e-551e3f12-1fa400-166c5a9f8bb165', ' fenqi_user_city': '36', ' ick_login': '6e768942-7af1-472a-932b-d603981de1d3', ' jebecookies': '63490022-6017-4399-bb56-8201a5512049|||||', ' _de': '03B1BEEBD7360E647318288C8F3F21C5', ' p': 'c5f8213bbd26ae8e90f0a9f8fd5386879', ' first_login_flag': '1', ' t': '824579c059d88caf3f86ff8b212da5389', ' societyguester': '824579c059d88caf3f86ff8b212da5389', ' id': '968526809', ' loginfrom': 'syshome', ' JSESSIONID': 'abcaZ9e3U_NeC6UpF_iBw', ' __utma': '151146938.1571025196.1540910644.1540970145.1540970145.1', ' __utmc': '151146938', ' __utmz': '151146938.1540970145.1.1.utmcsr=zhibo.renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/top', ' XNESSESSIONID': 'afc9f18ed618', ' xnsid': '36f791c1', ' jebe_key': '99fcaef9-a0c4-4f96-9c0a-080d66501e71%7Ce4cc5eaf1d0435f2177776fa256938dc%7C1540974668021%7C1', ' Hm_lvt_966bff0a868cd407a416b4e3993b9dc8': '1540910644,1540977210', ' Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8': '1540977919'}
            )

    def parse(self, response):
        print('='*30)
        print(type(response))
        req = response.request
        print(req.cookies)
        print(req.headers)
        with open('profile.html','w',encoding='utf-8') as f:
            f.write(response.text)


    # def parse_page(self, response):
    # 	url = "http://www.renren.com/968526809/profile"
    # 	yield scrapy.Request(url,callback=self.parse_profile)

    # def start_requests(self):
    # 	data = {"email":"18774979616","password":"wind2zero"}
    # 	for url in self.start_urls:
    # 		yield scrapy.FormRequest( url,dont_filter=True,
    # 			formdata=data,callback=self.parse_page)

    # def parse_profile(self,response):
    # 	with open('profile.html',"w",encoding="utf-8") as f:
    # 		f.write(response.text)