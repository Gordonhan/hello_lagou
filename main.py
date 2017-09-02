# -*- coding:utf-8 -*-
"""
@author: Gordon Han
@contact: Gordon-Han@hotmail.com
"""
from crawler.crawler import link_crawler
from crawler.scraping_callback import ScrapingCallback


if __name__ == '__main__':
    link_crawler(
        seed_url="https://www.lagou.com/zhaopin/Python/",
        delay=3,
        data={'filterOption': '3'},
        callback=ScrapingCallback(),
    )
