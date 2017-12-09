#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: mongo.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-1 下午9:04
 @desc: 
"""
from base import BaseDao

class MongoDao(BaseDao):
    def store(self, message):
        raise NotImplementedError()

    def get_message(self, id):
        raise NotImplementedError()