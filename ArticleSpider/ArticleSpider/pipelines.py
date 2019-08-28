# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from scrapy.pipelines.images import ImagesPipeline  # 图片下载模块
from scrapy.exporters import JsonItemExporter  # 导出json文件模块
import MySQLdb


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ArticleImagePipeline(ImagesPipeline):
    #重写该方法可从result中获取到图片的实际下载地址
    def item_completed(self, results, item, info):
        for ok , value in results:
            image_file_path = value["path"]
            print(ok,image_file_path)
        item["front_image_path"] = image_file_path

        return item

class JsonExporterPipleline(object):
    # 调用scrapy提供的json export导出json文件
    def __init__(self):  # __init__初始化
        self.file = open('articleexport.json', 'wb')  # wb 二进制打开方式
        self.exporter = JsonItemExporter(
            self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class GaoqingPipleline(object):
    def process_item(self, item, spider):
        return item
