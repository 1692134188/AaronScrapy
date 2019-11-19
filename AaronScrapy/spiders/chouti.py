# -*- coding: utf-8 -*-
import scrapy
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# A：首先我们需要创建一个类，并继承scrapy的一个子类：scrapy.Spider  或者是其他蜘蛛类型，后面会说到，除了Spider还有很多牛X的蜘蛛类型；
class ChoutiSpider(scrapy.Spider):
    name = 'chouti' # B：然后定义一个蜘蛛名，name=“”
    allowed_domains = ['chouti.com']
    start_urls = ['https://www.cnblogs.com/YK2012/default.html?page=2'] # C：定义我们需要爬取的网址，没有网址蜘蛛肿么爬

    def parse(self, response):
        print(response)
        print("Hello,Scrapy")


