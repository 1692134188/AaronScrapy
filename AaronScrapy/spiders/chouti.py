# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar

# A：首先我们需要创建一个类，并继承scrapy的一个子类：scrapy.Spider  或者是其他蜘蛛类型，后面会说到，除了Spider还有很多牛X的蜘蛛类型；
class ChoutiSpider(scrapy.Spider):
    name = 'chouti' # B：然后定义一个蜘蛛名，name=“”
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/'] # C：定义我们需要爬取的网址，没有网址蜘蛛肿么爬
    cookie_dict = None
    def parse(self, response):
        cookie_obj = CookieJar() #创建Cookie容器
        cookie_obj.extract_cookies(response,response.request)
        self.cookie_dict=cookie_obj._cookies
        yield Request(
            url="http://dig.chouti.com/login",
            method='POST',
            body="phone=8618896527725&password=yk2012&loginType=2",

            headers={'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",'Referer': "https://dig.chouti.com/",'User-Agent':" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400"},
            cookies=cookie_obj._cookies,
            callback=self.check_login
        )

    def check_login(self, response):
        print(response.text)
        yield Request(url="http://dig.chouti.com/", callback=self.good)



