# -*- coding: utf-8 -*-
import os
import time
import scrapy
from selenium import webdriver


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def __init__(self):
        self.login_cookies = []

    headers = {
        "Referer": "https://www.zhihu.com/signin?next=%2F",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }

    def get_cookies(self):
        project_dir = os.path.abspath(os.path.dirname(__file__))
        executable_path = os.path.join(project_dir, 'geckodriver.exe')
        # 知乎登录
        browser = webdriver.Firefox(executable_path=executable_path)
        time.sleep(3)
        browser.get("https://www.zhihu.com/signin?next=%2F")  # ①
        passwordButton=browser.find_element_by_xpath('//div[@class="SignFlow-tabs"]/div[@class="SignFlow-tab"]')
        passwordButton.click()
        time.sleep(1)

        # 获取输入用户名的文本框 
        elem_user = browser.find_element_by_xpath('//input[@name="username"]')
        # 模拟输入用户名
        elem_user.send_keys('18382409180')  # ②
        # 获取输入密码的文本框
        elem_pwd = browser.find_element_by_xpath('//input[@name="password"]')
        # 模拟输入密码
        elem_pwd.send_keys('jimkun2016')  # ③
        # 获取提交按钮
        commit = browser.find_element_by_xpath('//button[@type="submit"]')
        # 模拟单击提交按钮
        commit.click()  # ④
        # 暂停10秒，等待浏览器登录完成
        time.sleep(5)
        # 登录成功后获取cookie
        if "微博-随时随地发现新鲜事" in browser.title:
            self.login_cookies = browser.get_cookies()
        else:
            print("登录失败！")
    # start_requests方法会在parse方法之前执行，该方法可用于处理登录逻辑。

    def start_requests(self):
        self.get_cookies()
        print('=====================', self.login_cookies)
        # 开始访问登录后的内容
        return [
            scrapy.Request(
                'https://weibo.com/cyuyanzhongwenwang/',
                headers=self.headers,
                cookies=self.login_cookies,
                callback=self.parse
            )]
    # 解析服务器相应的内容

    def parse(self, response):
        print('~~~~~~~parse~~~~~')
        print("是否解析成功:", response.text)
