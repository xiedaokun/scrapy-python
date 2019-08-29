# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
import datetime
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value+'-bobby'


def date_convert(value):
    create_date = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", value).group(1)
    try:
        create_date = datetime.datetime.strptime(
            create_date, '%Y-%m-%d').date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def get_nums(value):
    match_re = re.match('.*?(\d+).*', value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


def remove_comment_tags(value):
    if '评论' in value:
        return ''
    else:
        return value


class GaoqingItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()


def return_value(value):
    return value


class GaoqingItem(scrapy.Item):
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    title = scrapy.Field(
        input_processor=MapCompose(lambda x: x+'-jobbole', add_jobbole)
    )
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    praise_nums = scrapy.Field(
        input_processor=MapCompose(lambda x: int(x))
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(lambda x: float(x))
    )
    content = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(',')
    )

    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_path = scrapy.Field()
    pass
