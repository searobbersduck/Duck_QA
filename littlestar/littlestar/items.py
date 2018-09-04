# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LittlestarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GamerankItem(scrapy.Item):
    rank = scrapy.Field()
    game = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    hot = scrapy.Field()


