# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlockScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    title = scrapy.Field()
    detail = scrapy.Field()

    print('test')
    print()
