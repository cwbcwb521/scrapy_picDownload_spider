# -*- coding: utf-8 -*-
import scrapy
from pic_pjt.items import PicPjtItem
from scrapy.http import Request
import re

CHECK_NEXT_URL = 1

class PicspdSpider(scrapy.Spider):
    name = "picspd"
    allowed_domains = ["58pic.com"]
    start_urls = (
        'http://www.58pic.com/c/14169081',
    )

    def parse(self, response):
        print('parse run')
        item = PicPjtItem()
        # 构建提取对应图片的正则
        patUrl = '(http://pic.qiantucdn.com/58pic/.*?.jpg)'
        # 提取对应图片网址
        item['pic_url'] = re.compile(patUrl).findall(str(response.body))
        # 构造出提取图片名的正则表达式，以方便构造本地文件名
        patLocal = 'http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg'
        # 提取互联网中的图片名
        item['pic_id'] = re.compile(patLocal).findall(str(response.body))
        yield item

        # 遍历图片列表
        global CHECK_NEXT_URL
        if CHECK_NEXT_URL == 1:
            CHECK_NEXT_URL = 0
            for i in range(1, 5):
                print('i:'+ str(i))
                nextUrl = 'http://www.58pic.com/c/14169081' + '?page=0' + str(i)
                yield Request(nextUrl, callback=self.parse)