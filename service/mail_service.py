#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: mail_service.py
 @author: ginger 
 @software: PyCharm
 @desc: 
"""

from service import Service
from model import object_builder
from utils.constants import *


class MailService(Service):
    def __init__(self,_dao,_email_senders):
        # 调用父类构造器
        Service.__init__(self,dao=_dao)
        self.__email_senders= _email_senders

    # def __initialize(self,send_id,_email_sender):  # config
    #     self.__email_senders[sender_id] = _email_sender



    def store_send_message(self,message):
        _mail_message = object_builder.message_build(message)
        # self.__dao.store(_mail_message)  # todo
        self.__email_senders[message[SENDER_ID]].send_message(_mail_message)