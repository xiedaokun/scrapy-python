# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

from ArticleSpider.items import JobBoleArticleItem

# 第四章7-15 01：07：00
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['zimuku.la']
    # start_urls = ['http://www.zimuku.la/detail/122420.html']
    start_urls = ['http://www.zimuku.la']

    def parse(self, response):
        """
        1.获取文章列表中的文章url并交给scrapy下载后进行解析
        2.获取下一页的url并交给scrapy进行下载，下载完成后就交给parse函数
        """

        # 解析列表页中所有文章url并交给scrapy下载后并进行解析
        post_nodes = response.css(".table tbody tr")
        for post_node in post_nodes:
            post_url = post_node.css("td.first>a::attr(href)").extract_first("")
            image_url = post_node.css("td.first div a img::attr(src)").extract_first("")

            post_url = parse.urljoin(response.url, post_url)
            image_url = parse.urljoin(response.url, image_url)
            yield Request(url=post_url, meta={"front_image_url": image_url}, callback=self.parse_detail)
        # 提取下一页
        # next_urls = response.css('.next::attr(href)').extract_first("")
        # if next_urls:
        #     yield Request(url=parse.urljoin(response.url, next_urls), callback=self.parse)

    def parse_detail(self, response):
        article_item = JobBoleArticleItem()

        # 提取文章的具体字段
        # # 标题
        # title = response.xpath('//div[@class="md_tt prel"]/h1/text()').extract()[0]
        # # 内容
        # content = response.xpath('//a[@class="gray"]/text()').extract()[0]
        # # 评分
        # give_sums = response.xpath('//div[@id="scinfo"]/i/b/text()').extract()[0]
        # # 下载次数
        # download_nums = response.xpath('//ul[@class="subinfo clearfix"]/li[3]/text()').extract()[0]
        # # 字母来源
        # source_letters = response.xpath('//ul[@class="subinfo clearfix"]/li[6]/span/text()').extract()[0]
        # # 上传时间
        # update_time = response.xpath('//ul[@class="subinfo clearfix"]/li[7]/text()').extract()[0].replace('By:','').strip()
        # 字幕大小
        # subtitle_size = response.css('#down1 small::text').extract()[0]

        # 封面图
        front_image_url = response.meta.get('front_image_url', '')
        first_image = 'http:' + response.css('.md_img>a>img::attr(src)').extract_first()
        # 标题
        title = response.css('div.md_tt.prel h1::text').extract()[0]
        # 内容
        content = response.css('a.gray::text').extract()[0]
        # 评分
        give_sums = response.css('#scinfo i b::text').extract()[0]
        give_sums = int(give_sums)
        # 下载次数
        download_nums = response.css('ul.subinfo.clearfix li:nth-child(3)::text').extract()[0]
        download_nums = int(download_nums)
        # 字母来源
        source_letters = response.css('ul.subinfo.clearfix li:nth-child(6) span::text').extract()[0]
        # 上传时间
        update_time = response.css('ul.subinfo.clearfix li:nth-child(7)::text').extract()[0].replace('By:', '').strip()
        # 字幕大小
        subtitle_size = response.css('#down1 small::text').extract()[0]

        article_item["title"] = title
        article_item["front_image_url"] = front_image_url
        article_item["first_image"] = [first_image]
        article_item["content"] = content
        article_item["url"] = response.url
        article_item["give_sums"] = give_sums
        article_item["download_nums"] = download_nums
        article_item["source_letters"] = source_letters
        article_item["update_time"] = update_time
        article_item["subtitle_size"] = subtitle_size

        yield article_item
