# -*- coding: utf-8 -*-

# Scrapy settings for rrlogin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'rrlogin'

SPIDER_MODULES = ['rrlogin.spiders']
NEWSPIDER_MODULE = 'rrlogin.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rrlogin (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
	"Cache-Control":"no-cache",
	"Connection":"keep-alive",
	"Cookie":"anonymid=jnvuek00-d8kdos; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1540910644; _ga=GA1.2.1571025196.1540910644; _gid=GA1.2.171189287.1540910644; _ga=GA1.3.1571025196.1540910644; _gid=GA1.3.171189287.1540910644; ln_uact=18774979616; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; depovince=HUN; _r01_=1; UM_distinctid=166c5a9f8ba100-09c5cc6d024b2e-551e3f12-1fa400-166c5a9f8bb165; fenqi_user_city=36; ick_login=6e768942-7af1-472a-932b-d603981de1d3; jebecookies=63490022-6017-4399-bb56-8201a5512049|||||; _de=03B1BEEBD7360E647318288C8F3F21C5; p=c5f8213bbd26ae8e90f0a9f8fd5386879; first_login_flag=1; t=824579c059d88caf3f86ff8b212da5389; societyguester=824579c059d88caf3f86ff8b212da5389; id=968526809; loginfrom=syshome; JSESSIONID=abcaZ9e3U_NeC6UpF_iBw; wp_fold=0; __utma=151146938.1571025196.1540910644.1540970145.1540970145.1; __utmc=151146938; __utmz=151146938.1540970145.1.1.utmcsr=zhibo.renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/top; XNESSESSIONID=afc9f18ed618; xnsid=36f791c1; jebe_key=99fcaef9-a0c4-4f96-9c0a-080d66501e71%7Ce4cc5eaf1d0435f2177776fa256938dc%7C1540974668021%7C1",
	"Host":"zhibo.renren.com",
	"Pragma":"no-cache",
	"Referer":"http://www.renren.com/968526809/profile",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
	"youhou":"fast"


}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'rrlogin.middlewares.RrloginSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'rrlogin.middlewares.RrloginDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'rrlogin.pipelines.RrloginPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
