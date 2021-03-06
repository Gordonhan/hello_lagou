# -*- coding:utf-8 -*-
"""
@author: Gordon Han
@contact: Gordon-Han@hotmail.com
"""
from downloader import Downloader
import urlparse


def link_crawler(seed_url, delay=3, data=None, callback=None):
    crawl_queue = [seed_url]
    seen = set()

    d = Downloader(delay)
    while crawl_queue:
        url = crawl_queue.pop()
        html = d(url, data)
        print html
        if callback:
            link = callback(html)
            if link is not None:
                url = link_format(seed_url, link)
                if url not in seen:
                    crawl_queue.append(url)
                    seen.add(url)


def link_format(url, link):
    return urlparse.urljoin(url, link)
