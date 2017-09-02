# -*- coding:utf-8 -*-
"""
@author: Gordon Han
@contact: Gordon-Han@hotmail.com
"""
import lxml.html


class ScrapingCallback(object):
    def __init__(self):
        pass

    def __call__(self, html):
        tree = lxml.html.fromstring(html)
        result = []
        jobs = tree.xpath(".//div[@id='s_position_list']/ul[@class='item_con_list']/li")
        print len(jobs)
        for job in jobs:
            company = job.xpath(".//div[@class='company_name']/a")[0].text_content()
            position = job.xpath(".//div[@class='position']//h3")[0].text_content()
            location = job.xpath(".//span[@class='add']/em")[0].text_content()
            salary = job.xpath(".//div[@class='li_b_l']//span")[0].text_content()
            experience = job.xpath(".//div[@class='li_b_l']")[0].text_content().strip()
            result.append({
                'company': company,
                'position': position,
                'salary': salary,
                'location': location,
                'experience': experience,
            })
        print result
        return tree.xpath(".//div[@id='s_position_list']//div[@class='pager_container']/a")[-1].get('href')
