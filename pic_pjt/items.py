# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PicPjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 建立 pic_url 存储图片的网址
    pic_url = scrapy.Field()
    # 建立 pic_id 存储图片网址中的图片名,方便构造本地文件名
    pic_id = scrapy.Field()
