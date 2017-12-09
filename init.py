#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: init_git.py
 @software: PyCharm  
 @time: 17-12-2 下午1:16
 @desc: 
"""

tasks_init = [
    {
        'task_id': 1,
        'sender_id': 11,
        'task_name': u'XXX',
        'description': u'Need to find a good Python tutorial on the web',
        'subject': u'XX',
        'receivers': ['jinjie603809@163.com']
    },
    {
        'task_id': 2,
        'sender_id': 12,
        'task_name': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'subject': u'XX',
        'receivers': [u'XXX@X.com',u'XXX@X.com']
    }
]

senders_init = [
    {
        'sender_id': 11,
        'mail_type': u'html',
        'passwd': 'XXX',
        'host': 'smtp.163.com',
        'username': 'xx@163.com'
    },
    {
        'sender_id': 12,
        'mail_type': u'html',
        'passwd': u'XX',
        'host': u'XX',
        'username': u'XX'
    }
]
