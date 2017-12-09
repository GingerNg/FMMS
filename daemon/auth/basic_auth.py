#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: basic_auth.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-3 下午1:49
 @desc: 
"""
from flask import make_response, jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'ok':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)