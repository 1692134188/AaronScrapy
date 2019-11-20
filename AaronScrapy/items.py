# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AaronscrapyItem(scrapy.Item):
    # 定义爬取的字段
    # name = scrapy.Field()
    name = scrapy.Field()
    ImgUrl = scrapy.Field()
    pass
