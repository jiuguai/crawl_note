import scrapy
from urllib.request import urlretrieve

class DbloginSpider(scrapy.Spider):
    name = 'dblogin'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']

    def parse(self, response):
        formdata = {
            "source": "None",
            "redir": "https://www.douban.com/",
            "form_email": "wind13zero@163.com",
            "form_password": "wind2zero",
            "login": "登录",
        }

        img_url = response.css('#captcha_image::attr(src)').get()
        captcha_id = response.css('input[name=captcha-id]::attr(value)').get()
        # with open('login.html','w',encoding='utf-8') as f:
        #   f.write(response.text)

        if img_url:
            urlretrieve(img_url,'validate.png')
            captcha_solution = input()
            formdata['captcha-solution'] = captcha_solution
            formdata['captcha-id'] = captcha_id
        print("="*30)
        print(captcha_id)
        print(img_url)
        url = "https://accounts.douban.com/login"
        yield scrapy.FormRequest(url,formdata=formdata,callback=self.login_parse)

    def login_parse(self,response):
        # with open('top.html','w',encoding='utf-8') as f:
        #   f.write(response.text)
        url = "https://www.douban.com/mine/"


        yield scrapy.Request(url,callback=self.profile_parse)

    def profile_parse(self,response):
        # with open('profile.html','w',encoding='utf-8') as f:
        #     f.write(response.text)
        path = response.xpath('//form[contains(@action,"edit_signature")]/@action').get()
        url = response.urljoin(path)
        ck = response.xpath('//input[@name="ck"]/@value').get()
        signature = '机器人修改'
        formdata = {
            "ck": ck,
            "signature": signature
        }
        print("="*30)
        print(url)

        yield scrapy.FormRequest(url,formdata=formdata,callback=self.none_parse)

    def none_parse(self,response):
        pass