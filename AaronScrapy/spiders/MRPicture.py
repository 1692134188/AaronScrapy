# -*- coding: utf-8 -*-
import scrapy
from  AaronScrapy.items import AaronscrapyItem

class MrpictureSpider(scrapy.Spider):
    name = 'MRPicture'
    allowed_domains = ['mm131.net']
    start_urls = ['http://www.mm131.net/xinggan/',
                  # 'http://www.mm131.net/qingchun/',
                  # 'http://www.mm131.net/xiaohua/',
                  # 'http://www.mm131.net/chemo/',
                  # 'http://www.mm131.net/qipao/',
                  # 'http://www.mm131.net/mingxing/'
                  ]
    def parse(self, response):
        list = response.css(".list-left dd:not(.page)")
        for img in list:
            imgname = img.css("a::text").extract_first()
            imgurl = img.css("a::attr(href)").extract_first()
            imgurl2 = str(imgurl)
            # next_url = response.css(".page-en:nth-last-child(2)::attr(href)").extract_first()
            # if next_url is not None:
            #     # 下一页
            #     yield response.follow(next_url, callback=self.parse)

            yield scrapy.Request(imgurl2, callback=self.content)

    def content(self, response):
        item = AaronscrapyItem()
        item['name'] = response.css(".content h5::text").extract_first()
        item['ImgUrl'] = response.css(".content-pic img::attr(src)").extract()
        yield item
        # 提取图片,存入文件夹
        # print(item['ImgUrl'])
        next_url = response.css(".page-ch:last-child::attr(href)").extract_first()

        if next_url is not None:
            # 下一页
            yield response.follow(next_url, callback=self.content)