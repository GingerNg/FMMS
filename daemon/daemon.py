#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: api.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-1 下午9:36
 @desc: 
"""
from flask import Flask, make_response, jsonify, request, abort
from flask_login import LoginManager

# from api.common import common
from mail.views import emails
from assembler import configure_app

# from auth.views import auth as auth_blueprint



app = Flask(__name__)
configure_app(app)

'''
auth
'''
login_manager = LoginManager()
login_manager.login_view = "auth"
login_manager.init_app(app)


app.register_blueprint(emails, url_prefix='/mail')
# api.register_blueprint(common, url_prefix='/')
# api.register_blueprint(auth_blueprint, url_prefix='/')

@app.route('/fortest', methods=['PUT'])
def fortest():
    if not request.json:
        abort(400)
    print request.json
    return jsonify({'status': 'received'})


@app.route('/')
def index():
    return '''
    welcome to FMSS
    '''

@app.route('/help')
def help():
    return '''
    /mail
    '''
# 全局
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# from flask import Flask, make_response,jsonify
# from flask_httpauth import HTTPBasicAuth
#
# auth = HTTPBasicAuth()
#
# @auth.get_password
# def get_password(username):
#     if username == 'ok':
#         return 'python'
#     return None
#
#
# @auth.error_handler
# def unauthorized():
#     api.logger.error("Unauthorized access")
#     return make_response(jsonify({'error': 'Unauthorized access'}), 401)









