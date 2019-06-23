# -*- coding: utf-8 -*-
import scrapy
from ..items import BlockScrapyItem


class BishijiespiderSpider(scrapy.Spider):
    name = 'bishijie'
    allowed_domains = ['bishijie.com']
    start_urls = ['https://www.bishijie.com/kuaixun']



    def parse(self, response):
        li_class = 'li.lh32'
        print(response)
        for form in response.css(li_class):
            bsj = BlockScrapyItem()
            bsj['href'] = form.xpath('./div/a/@href').extract_first()
            bsj['title'] = form.xpath('./h2/a/@title').extract_first()
            bsj['detail'] = form.xpath('./div/a/text()').getall()

            yield bsj

