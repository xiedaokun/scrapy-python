# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticleItem(scrapy.Item):
    url_object_id = scrapy.Field()
    first_image = scrapy.Field()  # 首图
    front_image_url = scrapy.Field()  # 封面图
    front_image_path = scrapy.Field()  # 封面图路径
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    give_sums = scrapy.Field()
    download_nums = scrapy.Field()
    source_letters = scrapy.Field()
    update_time = scrapy.Field()
    subtitle_size = scrapy.Field()


class ImagenetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    src = scrapy.Field()
    pass
