# -*- coding:utf-8 -*-
"""
@author: Gordon Han
@contact: Gordon-Han@hotmail.com
"""
import pymongo

from crawler.crawler import link_crawler
from crawler.scraping_callback import ScrapingCallback
from db.mongodb_cache import MongoCache


if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    cache = MongoCache(client=client)
    link_crawler(
        seed_url="https://www.lagou.com/zhaopin/Python/",
        delay=5,
        data={'filterOption': '3'},
        callback=ScrapingCallback(cache=cache),
    )
