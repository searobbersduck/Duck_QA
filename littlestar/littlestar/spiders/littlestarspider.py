#!/usr/bin/env python
# @Time    : 2018/8/8 上午11:17
# @Author  : SeaRobbersAndDuck
# @Site    : 
# @File    : littlestarspider.py
# @Software: PyCharm

import scrapy
from littlestar.items import GamerankItem
import time

class Gamerank(scrapy.Spider):
    name = 'ggame'
    allowed_domains = '9game.cn'
    start_urls = []
    for i in range(1,5):
        url = 'http://www.9game.cn/xyrb/'
        url = url + str(i) + '_0/'
        start_urls.append(url)
    print(start_urls)

    def parse(self, response):
        item = GamerankItem()
        time.sleep(4)
        games = response.xpath('//tr')
        for each_game in games:
            print(each_game)

