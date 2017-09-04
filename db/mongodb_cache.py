# -*- coding:utf-8 -*-
"""
@author: Gordon Han
@contact: Gordon-Han@hotmail.com
"""
import pymongo

from config import DB, DATA_COLL


class MongoCache(object):
    def __init__(self, client=None):
        self.client = client or pymongo.MongoClient('localhost', 27017)
        self.db = self.client[DB]
        self.collection = self.db[DATA_COLL]

    def insert(self, docs):
        self.collection.insert(docs)
