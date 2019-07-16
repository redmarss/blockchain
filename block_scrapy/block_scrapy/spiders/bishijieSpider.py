# -*- coding: utf-8 -*-
import scrapy
from ..items import BlockScrapyItem


class Bishijie_kuaixunSpider(scrapy.Spider):
    name = 'bishijie.kuaixun'
    allowed_domains = ['bishijie.com']
    start_urls = ['https://www.bishijie.com/kuaixun']

    def parse(self, response):
        #币世界/快讯
        for xdate in response.css('div.livetop'):
            date = xdate.attrib['class'][-10:]
            for form in xdate.xpath('./ul[@data-path_type="1"]'):
                bsj = BlockScrapyItem()
                bsj['source'] = 'bishijie.kuaixun'
                bsj['time'] = date + ' ' + form.xpath('./span/text()').extract_first()
                bsj['href'] = form.xpath('./li/h2/a/@href').extract_first()
                bsj['title'] = form.xpath('./li/h2/a/@title').extract_first()
                bsj['detail'] = form.xpath('./li/div/a/text()').extract_first()
                

                yield bsj

        #处理下一页


class Bishijie_biquanSpider(scrapy.Spider):
    name = "bishijie.biquan"
    allowed_domains = ['bishijie.com']
    start_urls = ["https://i.bishijie.com/hot"]
