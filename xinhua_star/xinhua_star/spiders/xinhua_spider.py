#!/usr/bin/env python
# @Time    : 2018/8/8 下午2:35
# @Author  : SeaRobbersAndDuck
# @Site    : 
# @File    : xinhua_spider.py
# @Software: PyCharm

import scrapy
from scrapy import Request
import time
import numpy as np
from xinhua_star.items import XinhuaStarItem
from scrapy.linkextractors import LinkExtractor
# from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.spiders import Rule, CrawlSpider

# class xinhua_spider(scrapy.Spider):
#     name='xinhuaspider'
#     base_url = 'http://www.xinhuanet.com/world/2018-08/07/c_1123236183.htm'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
#     }
#
#     start_urls = ['http://www.xinhuanet.com/world/2018-08/07/c_1123236183.htm' for i in range(10)]
#
#     # def start_requests(self):
#     #     yield Request(self.base_url, headers=self.headers)
#
#     def parse(self, response):
#         time.sleep(8)
#         artical = response.xpath('//tr')
#         print(artical)
#         print('parse')

class xinhua_spider(scrapy.Spider):
    time.sleep(1)
    name = 'xinhuaspider'
    base_url = 'http://www.xinhuanet.com/world/2018-08/07/c_1123236183.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    last_url = base_url
    list_crawled = []

    def start_requests(self):
        yield Request(self.base_url, headers=self.headers)

    def parse(self, response):
        next_urls = response.xpath('//div[@class="gotrain-container nav-ul"]/span/a/@href').extract()
        title = response.xpath('//div[@class="share-title"]/text()').extract()[0].strip()
        conts = response.xpath('//p/text()').extract()
        content = ''
        time_created = response.xpath('//span[@class="h-time"]/text()').extract()[0]
        for cont in conts:
            if cont == "":
                continue
            cont = cont.strip()
            if cont == "":
                continue
            content += cont
            content +='\n'
        print(u'抓取文章: ' + title)
        item = XinhuaStarItem()
        item['title'] = title
        item['content'] = content
        item['author'] = ''
        item['datetime'] = time_created
        yield item
        if self.last_url in next_urls:
            next_urls.remove(self.last_url)
        for i in range(len(next_urls)):
            next_url = np.random.choice(next_urls)
            if next_url not in self.last_url:
                break
        self.last_url = next_url
        if next_url:
            self.list_crawled.append(next_url)
            print('url:\t\t'+next_url)
            yield Request(next_url, headers=self.headers)
        else:
            print('No link more!!!!')

class xinhuarandom_spider(CrawlSpider):
    icnt = 0
    name = 'xinhuarandomspider'
    base_url = 'http://www.xinhuanet.com/world/2018-08/07/c_1123236183.htm'
    start_urls = [base_url]
    allowed_domains = ['xinhuanet.com']
    # rules后面是方括号！方括号！方括号！重要的事情说三遍！说三遍！说三遍！
    rules = [
        Rule(LinkExtractor(allow=('http:\/\/www.xinhuanet.com\/[\w]{1,}\/[0-9\-]{1,}\/[0-9]{1,}\/[\w0-9\-]{1,}.htm')),
             follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        item = XinhuaStarItem()
        try:
            next_urls = response.xpath('//div[@class="gotrain-container nav-ul"]/span/a/@href').extract()
            title = response.xpath('//div[@class="share-title"]/text()').extract()[0].strip()
            conts = response.xpath('//p/text()').extract()
            content = ''
            time_created = response.xpath('//span[@class="h-time"]/text()').extract()[0]
            for cont in conts:
                if cont == "":
                    continue
                cont = cont.strip()
                if cont == "":
                    continue
                content += cont
                content +='\n'
            # print('[{}]'.format(self.icnt) + u'抓取文章: ' + title + '\t\t' + time_created)
            item['title'] = title
            item['content'] = content
            item['author'] = ''
            item['datetime'] = time_created
            self.icnt += 1
            yield item
        except:
            ...
