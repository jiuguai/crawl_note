# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem
import json
from scrapy.http.response.html import HtmlResponse

HTML5_WHITESPACE = ' \t\n\r\x0c'
class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/trending/monthly?utm_medium=index-banner-s&utm_source=desktop']

    
    rules = (
        Rule(LinkExtractor(allow=r'/p/\w{12}',
            process_value=lambda x:x.split('?',1)[0],
            ), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'/p/31adf4813507',
        #     process_value=lambda x:x.split('?',1)[0],
        #     ), callback='parse_item'),
    )

    def parse_item(self, response):
        article = response.xpath('//div[@class="article"]')

        # 标题
        title = article.xpath('.//h1/text()').get()

        # 发布时间
        publish_time = article.xpath('.//span[@class="publish-time"]/text()').get()
        publish_time = publish_time.strip('*')
        # 当前页url
        page_url = response.url

        # 用户url
        user_home = response.urljoin( article.xpath('.//a[@class="avatar"]/@href').get())

        # 内容
        content = article.xpath('//div[@class="show-content-free"]').get()



        data_element = response.xpath('//script[@data-name="page-data"]')

        # 作者
        author = data_element.re(r'"nickname":"([^"]+)",')

        author = author[0] if author else ''

        # 字数
        words_count = data_element.re(r'"public_wordage":([^"]+?),')
        words_count = int(words_count[0]) if words_count else 0

        # 评论数
        comments_count = data_element.re(r'"comments_count":([^"]+?),')
        comments_count = int(comments_count[0]) if comments_count else ''

        # 喜欢数量
        likes_count = data_element.re(r'"likes_count":([^"]+?),')
        likes_count = int(likes_count[0]) if likes_count else 0

        # 阅读数
        views_count = data_element.re(r'"views_count":([^"]+?),')
        views_count = int(views_count[0]) if views_count else 0

        special_id = data_element.re(r'"id":([^"]+?),')
        special_id = int(special_id[0]) if special_id else 0
        special = response.xpath('//div[@class="include-collection"]/a/div/text()').getall()
        special = '|'.join([s.strip(' .') for s in special])
        print('='*30)
        print(special)
        print('='*30)
        
        item = JianshuItem(
            title = title,
            publish_time = publish_time,
            page_url = page_url,
            user_home = user_home,
            content = content,
            author = author,
            words_count = words_count,
            comments_count = comments_count,
            likes_count = likes_count,
            views_count = views_count,
            special_id =special_id,
            special = special,
        )
        yield item

    def parse_special(self,response):
        # TEMPLATE_SPECIAL_URL = "https://www.jianshu.com/notes/%s/included_collections?page=%s"
        # url = self.TEMPLATE_SPECIAL_URL %(page_id,1)
        # request = scrapy.Request(url=url,callback=self.parse_special)
        # request.meta['item'] = item
        # request.meta['special'] = []
        # request.meta['page_id'] = page_id


        special_d = json.loads(response.text)
        if 'special' not in response.meta:
            special =  []
        else :
            special = response.meta['special']

        special.extend([d['title'] for d in special_d['collections']])

        if special_d['page'] >= special_d['total_pages']:
            
            print('='*30)
            print(special)
            print(response.url)
            item = response.meta['item']
            item['special'] = ' | '.join(special)

            
            yield item
        else:
            page_id = response.meta['page_id']
            url = self.TEMPLATE_SPECIAL_URL %(page_id,special_d['page']+1)
            request = scrapy.Request(url,callback=self.parse_special)
            request.meta['special'] = special
            request.meta['page_id'] = page_id
            request.meta['item'] = response.meta['item']
            request.headers = response.request.headers
            yield request

class JssSpider(scrapy.Spider):
    name = 'jss'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/notes/34246320/included_collections?page=1']
    
    TEMPLATE_SPECIAL_URL = "https://www.jianshu.com/notes/34246320/included_collections?page=%s"

    def parse(self,response):
        special_d = json.loads(response.text)
        if 'special' not in response.meta:
            special =  []
        else :
            special = response.meta['special']
        

        special.extend([d['title'] for d in special_d['collections']])

        if special_d['page'] >= special_d['total_pages']:

            special = ' | '.join(special)
            print('='*30)
            print(special)
             

        else:
            url = self.TEMPLATE_SPECIAL_URL %(special_d['page']+1)
            request = scrapy.Request(url,callback=self.parse)
            request.meta['special'] = special
            
            yield request