import scrapy
import re


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']

    headers = {
        "HOST": "www.zhihu.com",
        'Referer': 'https://www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
    }
    custom_settings = {
        "COOKIES_ENABLED": True
    }

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/#sigin', headers=self.headers, callback=self.login)]

    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"',
                             response_text, re.DOTALL)
        if match_obj:
            xsrf = (match_obj.group(1))

        if xsrf:
            post_data = {
                '_xsrf': xsrf,
                'phone_num': '',
                'capcha': ''
            }
            import time
            t = str(int(time.time()*100))
            captcha_url = 'https://www.zhihu.com/captcha.gif?r={0}&type=login'.format(
                t)
            yield scrapy.Request(captcha_url, headers=self.headers, meta={'post_data': post_data}, callback=self.login_after_captcha)

    def login_after_captcha(self,response):
        pass

    def parse(self, response):
        pass
