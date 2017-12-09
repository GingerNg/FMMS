#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: auth.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-3 上午1:59
 @desc: 
"""
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask import make_response,jsonify
"""
self-defined user
"""

class User(UserMixin):
    def get_id(self):
        return 1

SingleAuthUser = User()


# @login_manager.user_loader
# def load_user(userid):
#     return SingleAuthUser

