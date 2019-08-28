# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import GaoqingItem
from ArticleSpider.utils.common import get_md5

class GaoqingSpider(scrapy.Spider):
    name = 'gaoqing'
    allowed_domains = ['gaoqing.fm']
    start_urls = ['https://gaoqing.fm/']

    def parse(self, response):
        post_nodes=response.css('#result1 li div.pull-left.x-movie-mediumimg>a')
        for post_node in post_nodes:
            #获取封面图的url
            image_url=post_node.css('div>img::attr(src)').extract_first()
            post_url=post_node.css('::attr(href)').extract_first()
            yield Request(url=parse.urljoin(response.url,post_url),meta={'front_image_url':image_url},callback=self.parse_detail)

    def parse_detail(self,response):
        # 提取文章的具体字段
        """         # 标题
        title = response.xpath('//*[@id="mainrow"]//h2/a/text()').extract_first()
        #上映时间
        create_date = response.xpath('//*[@id="viewfilm"]/span[contains(text(),"上映")]/following-sibling::a/text()').extract_first()
        # 推荐数
        praise_nums = response.xpath('//*[@id="like"]/span[@class="fm-opt-label"]/text()').extract_first()
        # 想看
        fav_nums = response.xpath('//*[@id="plan"]/span[@class="fm-opt-label"]/text()').extract_first()
        # 评分
        comment_nums = response.xpath('//*[@id="viewfilm"]/span[contains(text(),"评分")]/following-sibling::span/text()').extract_first()
        # 剧情介绍
        content = response.xpath('//*[@id="des-full"]/text()').extract_first().strip()

        tag_list =  response.xpath("//*[@id='result1']/a/span[@class='fm-opt-label']/text()").extract()
        tag_list_label = response.xpath("//*[@id='result1']/a/text()").extract()
        tags = ",".join(tag_list_label) """

        front_image_url=response.meta.get('front_image_url','')
        title = response.css("#mainrow h2 > a::text").extract_first()
        create_date = response.css("#viewfilm>span:contains('上映')+a::text").extract_first()
        praise_nums = response.css("#like>span.fm-opt-label::text").extract_first()
        fav_nums = response.css("#plan>span.fm-opt-label::text").extract_first()
        comment_nums = response.css("#viewfilm>span:contains('评分')+span::text").extract_first()
        content = response.css("#des-full::text").extract_first().strip()
        # tag_list = response.css("#result1>a>span.fm-opt-label::text").extract()
        tag_list_label = response.css("#result1>a>::text").extract()
        tags = ",".join(tag_list_label)

        gaoqing_item=GaoqingItem()
        gaoqing_item['front_image_url']=[front_image_url]
        gaoqing_item['title']=title
        gaoqing_item['create_date']=create_date
        gaoqing_item['praise_nums']=praise_nums
        gaoqing_item['fav_nums']=fav_nums
        gaoqing_item['comment_nums']=comment_nums
        gaoqing_item['content']=content
        gaoqing_item['tags']=tags

        gaoqing_item['url_object_id']=get_md5(response.url)

        yield gaoqing_item
