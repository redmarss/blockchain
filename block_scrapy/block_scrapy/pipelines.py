# -*- coding: utf-8 -*-
import pymysql.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BlockScrapyPipeline(object):
    def process_item(self, item, spider):
        #去除item['href']的第一个字符‘/’
        item['href'] = item['href'][1:]
        #去除item['detail']左右空格
        item['detail'] = "".join(item['detail']).strip()
        #处理title 及 detail中的引号或双引号
        item['title'] = pymysql.escape_string(item['title'])
        item['detail'] = pymysql.escape_string(item['detail'])

        return item


class MySQLPipeline(object):
    def __init__(self):
        #连接数据库
        self.connect = pymysql.connect(
            host='cdb-iar6zzqb.gz.tencentcdb.com',
            port=10141,
            db='blockchain',
            user='root',
            passwd='888@XyFxBm',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        sql_select = f"select * from news where news_id = '{item['href']}'"
        self.cursor.execute(sql_select)
        result = self.cursor.fetchall()
        if len(result) == 0:
            try:
                sql = f"insert into news(news_id,time,source,title,detail) value ('{item['href']}','{item['time']}','{item['source']}','{item['title']}','{item['detail']}')"
                self.cursor.execute(sql)
                self.connect.commit()
                return item
            except:
                print('error')