# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
import MySQLdb


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()

# 同步操作
class MysqlPipline(object):
    def __init__(self):
        # 链接数据库
        self.conn = MySQLdb.connect(
            '127.0.0.1', 'root', '', 'article_spider', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(url_object_id,first_image,title,content)
            VALUES (%s,%s,%s,%s)
        """
        self.cursor.execute(
            insert_sql, (
                item['url_object_id'],
                item['first_image'],
                item['title'],
                item['content'],
            ))
        self.conn.commit()

# 异步操作

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


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
            item['front_image_path'] = image_file_path
        return item
