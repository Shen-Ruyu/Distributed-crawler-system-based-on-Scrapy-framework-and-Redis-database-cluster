# -*- coding: utf-8 -*-

BOT_NAME = 'weibo_spider'

SPIDER_MODULES = ['weibo_spider']
NEWSPIDER_MODULE = 'weibo_spider'

ROBOTSTXT_OBEY = False

# cookie = "XSRF-TOKEN=56RLvgqIlfpyyiONiMfyFVuF; WBPSESS=Wk6CxkYDejV3DDBcnx2LOUuyjUb5ny6U8XGAETh1XBU7V1a0-fhQuL49hmFCzrbH5AeFthlj2ysGiR9pALdDjS8hgDPxu_X2lRFoH9dDJI1jQ37tN9yykey5im45ByyWWMuzuc0ps3zwtwlSwHnSqM9k28im52Zen8l44xYGkIU=; SUB=_2A25LXPX2DeRhGeFI7lAQ8S7JzjSIHXVoEHc-rDV8PUNbmtAGLXLdkW9NfRwIdF9iPkVAQBL4b7aYvKR6MGeuFxGh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW3gJQ0VAY5QC4H1bR7I7ly5JpX5KzhUgL.FoMcSKzpeK5fSKn2dJLoIpqLxK-LBo5L12qLxK.LBKeL12HkeK-c; ALF=02_1719669414"
cookie = "SINAGLOBAL=1701842768202.8215.1620022420516; ULV=1716221748230:4:1:1:786927680192.9259.1716221748226:1713877319005; UOR=,,cn.bing.com; SCF=AkyS6Ejwpay8p8wtiyTigVUecHWBcT6TktDrW6bhLEY9dQH5L-lAsM07IRhK-4gyBwXAXu06DM20pbcNaEWyXHw.; SUB=_2A25KIkITDeRhGeNM6VEV8CnFzTuIHXVpXtvbrDV8PUNbmtANLU3YkW9NTiFIl0j4MGAjrS6S_jiSO5l1-f8eA1hK; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFmSuupMfWsm6G2i69zNlpB5JpX5KzhUgL.Fo-EeoeXehM4SoM2dJLoI0qLxKML1KBLB.zLxK.LBKeL12-LxKBLB.2LB.2LxKMLB-BL1h.LxK.LBKeL12-LxKqL1-BLBK-t; ALF=02_1733148483; XSRF-TOKEN=gRPFJ1UmpnFO03xxSoivpJmA; WBPSESS=B_i2-yUFdTgdfYAbzYpCqWb6VZxA07y1S1PR75JNt2-ldf3EQ1ZgVNxuj36NWJ5R-Ez746Z6GJ8KBZaQSn68If5RQBsAKDswjf2eJmkfc1lwmvy8QrzId8EjMxFFRh5Mb4LVBw9E57APFcH4SMSqvA=="

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    # 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    'Cookie': cookie
}

# 使用Redis调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 使用Redis去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 指定Redis连接信息
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# 允许中断恢复
SCHEDULER_PERSIST = True

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'weibo_spider.middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    # 'weibo_spider.pipelines.JsonWriterPipeline': 300,
    'weibo_spider.pipelines.RedisPipeline': 299,
}


