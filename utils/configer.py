#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: configer.py
 @author: ginger 
 @software: PyCharm
 @desc: 
"""
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import logging
import yaml
from utils.constants import CONFIG_NAME



def get_config_file():
    config_file_path = os.path.join(BASE_DIR, CONFIG_NAME)
    to_load = open(config_file_path)
    config = yaml.load(to_load.read())
    to_load.close()
    return config


def get_conf(config, path, default=None):
    current = config
    for level in path.split('.'):
        if level not in current:
            msg = 'Defaulting missing config key %s to %s' % (path, default)
            print msg
            logging.warning(msg)
            return default
        current = current[level]
    return current
