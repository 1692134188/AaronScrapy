# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class AaronscrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AaronscrapyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # referer = 'https://www.mm131.net/xinggan/5261_35.html'
        referer = 'https://www.cnblogs.com'
        if referer:
            request.headers['referer'] = referer
        request.headers['origin']= 'https://www.cnblogs.com'
        request.headers['accept'] = 'application/json, text/javascript, */*; q=0.01',
        request.headers['accept-encoding'] = 'gzip, deflate, br',
        request.headers['accept-language'] = 'zh-CN,zh;q=0.9',
        request.headers['content-length'] = '57',
        request.headers['content-type'] = 'application/json; charset=UTF-8',
        request.headers['cookie'] = '_ga=GA1.2.120698190.1574043617; _gid=GA1.2.881794986.1574043617; __gads=ID=b3400cd1d1125576:T=1574043617:S=ALNI_MYLicUrLg_GEnVq73lUvyThMIiwXQ; UM_distinctid=16e8266dd04357-0bb1cea8f1da75-7711a3e-144000-16e8266dd055f; CNZZDATA1254128672=922290337-1574142118-https%253A%252F%252Fwww.cnblogs.com%252F%7C1574142118; .Cnblogs.AspNetCore.Cookies=CfDJ8DeHXSeUWr9KtnvAGu7_dX-d2rsnpf8J9I9IQe1ONx8WSQqP6_GFPRfxDTprXd16jqTreqWRRkisDEEf_ukSAeFJ4PNNuS8CMwHTuH9nbe672ym7WHHpZCuREd5zFXkguV4iE5gUrnHV52yIgwR3ST6h3oFU3CFzq6tHepq0flaIjSyMach475GPtPrh9xWPebgmQsJ3GK1RToMitXoy4c6Y1yjmipepEzgz0cCs9sZ0Un16-tawfhZleob2YC2Quek0zgSTuvaiRlFtIlSFvHmCIEyoieEY0_qRf8oXBJ-E7p-PDRf8_Dnm9VSUutDzlSIb3IxcX9R6Inz-7o42vfhStVyOsAw8GL6NrAZo6pOGlbbjE3wB7OqChTCjloT5sqhJqCyMAaeqOQwh0PeNBLF1JJQzQhQwOI3GB7bKirSBckbGPF0USj9jYAOVssuOtSm0rg-xjuAWA-q6s3LTrkOrDAdZwrEihH891IzhlgE2uXY4Xlig79shCxJF8joPzRNVkudwXeJWq_9ryciKbZ6eIrvTbQ02xyKvZZbbGP6j; .CNBlogsCookie=CA4253E8DC05AABC6DBE79F2166571EA2089BF6DEC9B73BEF8A1C2E9E462F82A316B20E3B610B1DB5B6B693DCCD9AC737DD16074326D0D0F3B8B2F61155C0F61FFFE0DEAA3EE17081FA0F9D868DDE2C42E64F633; _gat=1',
        request.headers['origin'] = 'https://www.cnblogs.com',
        request.headers['referer'] = 'https://www.cnblogs.com/',
        request.headers['sec-fetch-mode'] = 'cors',
        request.headers['sec-fetch-site'] = 'same-origin',
        request.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        request.headers['x-requested-with']= 'XMLHttpRequest',


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
