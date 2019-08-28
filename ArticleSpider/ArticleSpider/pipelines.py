# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from scrapy.pipelines.images import ImagesPipeline  # scrapy图片自定义下载模块
from scrapy.exporters import JsonItemExporter  # scrapy导出json文件模块
import MySQLdb


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleImagePipeline(ImagesPipeline):
    # 重写该方法可从result中获取到图片的实际下载地址
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value["path"]
            print(ok, image_file_path)
        item["front_image_path"] = image_file_path

        return item

# python提供的json导出文件


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 将item转换为dict，然后生成json对象，false避免中文出错
        lines = json.dumps(dict(item), ensure_ascii=False)+'\n'
        self.file.write(lines)
        return item
    # 当spider关闭的时候

    def spider_closed(self, spider):
        self.file.close()

# scrapy提供的json导出文件


class JsonExporterPipleline(object):

    def __init__(self):  # __init__初始化
        self.file = open('articleexport.json', 'wb')  # wb 二进制打开方式
        self.exporter = JsonItemExporter(
            self.file, encoding='utf-8', ensure_ascii=False
        )
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MysqlPipline(object):

    # 采用同步的机制写入mysql
    def __init__(self):
        self.conn = MySQLdb.connect(
            '127.0.0.1',
            'root',
            '',
            'article_spider',
            charset="utf8",
            use_unicode=True
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(
                front_image_url,
                title,
                create_date,
                praise_nums,
                fav_nums,
                comment_nums,
                content,
                tags,
                url_object_id
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql, (
            item["front_image_url"],
            item["title"],
            item["create_date"],
            item["praise_nums"],
            item["fav_nums"],
            item["comment_nums"],
            item["content"],
            item["tags"],
            item["url_object_id"]
        ))
        self.conn.commit()
        return item

# class GaoqingPipleline(object):
#     def process_item(self, item, spider):
#         return item
