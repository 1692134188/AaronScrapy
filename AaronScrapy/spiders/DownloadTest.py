# -*- coding: utf-8 -*-
import scrapy
from AaronScrapy.items import AaronscrapyItem


class DownloadtestSpider(scrapy.Spider):
    name = 'DownloadTest'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls =  ['http://lab.scrapyd.cn/archives/55.html',
                  'http://lab.scrapyd.cn/archives/57.html',
                  ]

    def parse(self, response):
        item = AaronscrapyItem() #实例化Item
        imgurls = response.css(".post-content img::attr(src)").extract() #这里是一个集合，含有多张图片
        item['ImgUrl'] = imgurls
        name = response.css(".post-title a::text").extract_first()
        item['name'] = name
        yield item
