# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class PicPjtPipeline(object):
    def process_item(self, item, spider):
        # 依次将图片列表中的图片存储到本地
        for i in range(0, len(item['pic_url'])):
            this_pic = item['pic_url'][i]
            # 构造出图片在本地存储的地址
            localpath = '/Users/slothgreed/scrapy_study/scrapy_workplace/pic_pjt/picDown/' + item['pic_id'][i] + '.jpg'
            # 通过 urllib.request.urlretrieve()将原图下载
            urllib.request.urlretrieve(this_pic, localpath)

        return item
