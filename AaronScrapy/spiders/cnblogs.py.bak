# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# A：首先我们需要创建一个类，并继承scrapy的一个子类：scrapy.Spider  或者是其他蜘蛛类型，后面会说到，除了Spider还有很多牛X的蜘蛛类型；
class ChoutiSpider(scrapy.Spider):
    name = 'cnblogs' # B：然后定义一个蜘蛛名，name=“”
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/wupeiqi/default.html?page=1'] # C：定义我们需要爬取的网址，没有网址蜘蛛肿么爬

    def parse(self, response):

        HeaderTitle=  response.css('#Header1_HeaderTitle')[0]
        autor= HeaderTitle.css('::text').extract_first()  #作者
        articles = response.css('div.day')
        for article in articles:
            time=article.css('.dayTitle a::text').extract_first()  # 时间
            title = article.css('.postTitle2::text').extract_first() #标题
            fileName = '%s-随笔.txt' % autor  # 爬取的内容存入文件，文件名为：作者-随笔.txt
            f = open(fileName, "a+")  # 追加写入文件
            f.write(time.strip()+"            "+title.strip())  # 写入标签
            f.write('\n')  # 换行
        f.close()  # 关闭文件操作
        #  < a href = "https://www.cnblogs.com/YK2012/default.html?page=20" > 下一页 < / a >
        pages = response.css('#homepage_top_pager .pager a')
        next_page = None
        for page in pages:
            if(page.css('::text').extract_first().strip()=="下一页"):
                next_page=page.css('::attr(href)').extract_first().strip()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



