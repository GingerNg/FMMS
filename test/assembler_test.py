#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from flask import Flask
from assembler import *

app = Flask(__name__)
configure_app(app)
