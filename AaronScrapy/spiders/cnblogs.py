# -*- coding: utf-8 -*-
import scrapy
import re
import json
import base64

from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.http.cookies import CookieJar


# A：首先我们需要创建一个类，并继承scrapy的一个子类：scrapy.Spider  或者是其他蜘蛛类型，后面会说到，除了Spider还有很多牛X的蜘蛛类型；
class ChoutiSpider(scrapy.Spider):
    name = 'cnblogs'  # B：然后定义一个蜘蛛名，name=“”
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/qiuyu666/p/11903768.html']  # C：定义我们需要爬取的网址，没有网址蜘蛛肿么爬

    def parse(self, response):
        yield Request(
            url="https://www.cnblogs.com/qiuyu666/ajax/vote/blogpost",
            method='POST',
            body="""isAbandoned=false&postId=11903768&voteType=Digg""",

            cookies={'CNZZDATA1254128672': '922290337-1574142118-https%253A%252F%252Fwww.cnblogs.com%252F%7C1574142118',
                     '.Cnblogs.AspNetCore.Cookies': 'CfDJ8DeHXSeUWr9KtnvAGu7_dX-d2rsnpf8J9I9IQe1ONx8WSQqP6_GFPRfxDTprXd16jqTreqWRRkisDEEf_ukSAeFJ4PNNuS8CMwHTuH9nbe672ym7WHHpZCuREd5zFXkguV4iE5gUrnHV52yIgwR3ST6h3oFU3CFzq6tHepq0flaIjSyMach475GPtPrh9xWPebgmQsJ3GK1RToMitXoy4c6Y1yjmipepEzgz0cCs9sZ0Un16-tawfhZleob2YC2Quek0zgSTuvaiRlFtIlSFvHmCIEyoieEY0_qRf8oXBJ-E7p-PDRf8_Dnm9VSUutDzlSIb3IxcX9R6Inz-7o42vfhStVyOsAw8GL6NrAZo6pOGlbbjE3wB7OqChTCjloT5sqhJqCyMAaeqOQwh0PeNBLF1JJQzQhQwOI3GB7bKirSBckbGPF0USj9jYAOVssuOtSm0rg-xjuAWA-q6s3LTrkOrDAdZwrEihH891IzhlgE2uXY4Xlig79shCxJF8joPzRNVkudwXeJWq_9ryciKbZ6eIrvTbQ02xyKvZZbbGP6j',
                     '.CNBlogsCookie': 'CA4253E8DC05AABC6DBE79F2166571EA2089BF6DEC9B73BEF8A1C2E9E462F82A316B20E3B610B1DB5B6B693DCCD9AC737DD16074326D0D0F3B8B2F61155C0F61FFFE0DEAA3EE17081FA0F9D868DDE2C42E64F633'},
            callback=self.check_result
        )

    def check_result(self, response):
        print(response.text)
