# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapy.http.response.html import HtmlResponse
class JianshuDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    service_args =[
                    '--load-images=false',
                    '--max-disk-cache-size=1000',
                    '--disk-cache=true'
                ]
    def __init__(self):
        # self.driver = webdriver.PhantomJS(service_args=self.service_args)
        self.driver = webdriver.Chrome(service_args=self.service_args)
        self.wait = WebDriverWait(self.driver, 2.7)



    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called


        # driver_path = r"E:\Python\driver\chromedriver.exe"
        # driver = webdriver.Chrome(executable_path=driver_path)
        
        self.driver.get(request.url)

        while True:
            try:

                show = self.wait.until( 
                        EC.presence_of_element_located((By.CSS_SELECTOR,'.show-more'))
                    )
                show.click()
                driver.implicitly_wait(0.1)
            except:
                response = HtmlResponse(url=request.url,body=self.driver.page_source,request=request,encoding='utf-8')
                
                return response
            
    def __del__(self):
        self.driver.quit()