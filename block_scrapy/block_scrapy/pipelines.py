# -*- coding: utf-8 -*-
import pymysql.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BlockScrapyPipeline(object):
    def process_item(self, item, spider):
        item['href'] = item['href'][1:]
        item['detail'] = " ".join(item['detail']).strip()
        #处理title 及 detail中的引号或双引号
        item['title'] = pymysql.escape_string(item['title'])
        item['detail'] = pymysql.escape_string(item['detail'])
        return item


class MySQLPipeline(object):
    def __init__(self):
        #连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='blockchain',
            user='root',
            passwd='redmarss',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        sql_select = f"select * from news where news_id = '{item['href']}'"
        self.cursor.execute(sql_select)
        result = self.cursor.fetchall()
        if len(result)==0:
            sql = f"insert into news(news_id,time,title,detail) value ('{item['href']}','{item['time']}','{item['title']}','{item['detail']}')"
            self.cursor.execute(sql)
            self.connect.commit()
            return item
