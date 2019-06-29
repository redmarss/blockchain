# -*- coding: utf-8 -*-
import scrapy
from ..items import BlockScrapyItem


class BishijiespiderSpider(scrapy.Spider):
    name = 'bishijie'
    allowed_domains = ['bishijie.com']
    start_urls = ['https://www.bishijie.com/kuaixun']



    def parse(self, response):
        date = response.css('div.livetop').attrib['class'][-10:]

        for form in response.xpath('//ul[@data-path_type="1"]'):
            bsj = BlockScrapyItem()
            # bsj['time'] = form.xpath()
            # bsj['href'] = form.xpath('./div/a/@href').extract_first()
            # bsj['title'] = form.xpath('./h2/a/@title').extract_first()
            # bsj['detail'] = form.xpath('./div/a/text()').getall()
            bsj['time'] =date + ' ' + form.xpath('./span/text()').extract_first()
            bsj['href'] = form.xpath('./li/h2/a/@href').extract_first()
            bsj['title'] = form.xpath('./li/h2/a/@title').extract_first()
            bsj['detail'] = form.xpath('./li/div/a/text()').extract_first()

            yield bsj

        #处理下一页