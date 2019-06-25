# -*- coding: utf-8 -*-
import scrapy
from ..items import BlockScrapyItem


class BishijiespiderSpider(scrapy.Spider):
    name = 'bishijie'
    allowed_domains = ['bishijie.com']
    start_urls = ['https://www.bishijie.com/kuaixun']



    def parse(self, response):

        for form in response.css('div.livetop'):
            bsj = BlockScrapyItem()
            # bsj['time'] = form.xpath()
            # bsj['href'] = form.xpath('./div/a/@href').extract_first()
            # bsj['title'] = form.xpath('./h2/a/@title').extract_first()
            # bsj['detail'] = form.xpath('./div/a/text()').getall()
            date = form.attrib['class'][-10:]
            bsj['time'] =date + ' ' + form.xpath('./ul/span/text()').extract_first()
            bsj['href'] = form.xpath('./ul/li/h2/a/@href').extract_first()
            bsj['title'] = form.xpath('./ul/li/h2/a/@title').extract_first()
            bsj['detail'] = form.xpath('./ul/li/div/a/text()').getall()

            yield bsj

        #处理下一页