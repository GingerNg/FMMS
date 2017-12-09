#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: base.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-1 下午8:50
 @desc: 
"""
class BaseDao(object):

    def store(self, message):
        raise NotImplementedError()

    def get_message(self, id):
        raise NotImplementedError()
