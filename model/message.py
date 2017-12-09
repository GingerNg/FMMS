#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: message.py
 @author: ginger 
 @software: PyCharm
 @desc: 
"""
class Message(object):
    def __init__(self, subject,receivers,content):
        self.__subject = subject
        self.__receivers = receivers
        self.__content = content

    def get_subject(self):
        return self.__subject

    def get_receivers(self):
        return self.__receivers

    def get_content(self):
        return self.__content

