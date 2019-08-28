# -*- coding: utf-8 -*-
import scrapy
import re


class GaoqingSpider(scrapy.Spider):
    name = 'gaoqing'
    allowed_domains = ['gaoqing.fm']
    start_urls = ['https://gaoqing.fm/view/3db464eea2d3']

    def parse(self, response):

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
    
        title = response.css("#mainrow h2 > a::text").extract_first()
        create_date = response.css("#viewfilm>span:contains('上映')+a::text").extract_first()
        praise_nums = response.css("#like>span.fm-opt-label::text").extract_first()
        fav_nums = response.css("#plan>span.fm-opt-label::text").extract_first()
        comment_nums = response.css("#viewfilm>span:contains('评分')+span::text").extract_first()
        content = response.css("#des-full::text").extract_first().strip()
        tag_list = response.css("#result1>a>span.fm-opt-label::text").extract()
        tag_list_label = response.css("#result1>a>::text").extract()
        tags = ",".join(tag_list_label)

        pass
