#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import jieba
jieba.load_userdict('./block_scrapy/dict/myword.txt')

class DataClean(object):
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

    #重写数据库中tag字段，与最新的tagword对应
    def cleanTag(self):
        sql = 'select news_id from news where tag is null'
        self.cursor.execute(sql)
        t = self.cursor.fetchall()[:]
        print(t)



if __name__ == '__main__':
    dc = DataClean()
    dc.cleanTag()

