#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: assembler.py
 @author: ginger 
 @software: PyCharm
 @desc: 
"""
import logging
from model.email_sender import EmailSender
from service.mail_service import MailService
from utils.constants import *
from dao.mongo import MongoDao
from init import senders_init
from utils.configer import *
import yaml
from utils.constants import APP_HOST, APP_PORT, USE_RELOADER, APP_DEBUG



def configure_app(app):
    config = get_config_file()
    app.debug = get_conf(config, APP_DEBUG)
    app.config[APP_HOST] = get_conf(config, APP_HOST, '127.0.0.1')
    app.config[APP_PORT] = get_conf(config, APP_PORT, '9000')
    app.config[USE_RELOADER] = get_conf(config, USE_RELOADER, False)
    print get_conf(config, APP_PORT)


def configure_senders():
    for sender in senders_init:
        _senders = EmailSender(host=sender[HOST],username=sender[USERNAME],
                               mail_type=sender[MAIL_TYPE],passwd=sender[PASSWORD],
                               sender_id=sender[SENDER_ID])
        _senders_list[sender[SENDER_ID]] = _senders

def init_logger(location,config):
    pass


_senders_list = {}
configure_senders()
_dao = MongoDao()
service = MailService(_dao=_dao,_email_senders=_senders_list)
