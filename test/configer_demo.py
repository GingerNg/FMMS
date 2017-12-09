#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from utils.configer import get_config_file

if __name__ == '__main__':
    print (get_config_file())