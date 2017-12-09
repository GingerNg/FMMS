#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: auth.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-1 下午8:24
 @desc: 
"""
import copy
import logging
import time

from flask import Blueprint, abort, request, url_for, jsonify

from assembler import service
from init import tasks_init as tasks
from utils.constants import *
from daemon.auth.basic_auth import auth

emails = Blueprint('email', __name__, '/mail')

'''
todo --- mysql
send_email(host, username, passwd, send_to, subject, content)
'''


@emails.route('/')
def index():
    return '''
    Welcome to FSM/Mail  <br />
    You can get help via /mail/help using <GET>
    '''


@emails.route('/help')
def help():
    return jsonify({
    'This service provides functions as below': '',
    'Fetch_the_information_of_all_task': '/mail/tasks <GET>',
    'fetch_the_information_of_one_task via task_id': '/mail/task/task_id  <GET>',
    'activate_one_task_via_task_id': '/mail/task/task_id  <POST>',
    'register_task': '/mail/register_task <POST>'
    })


@emails.route('/register_task')
def add_task():
    pass

@emails.route('/tasks', methods=['GET'])
@auth.login_required
# @login_required
def get_tasks():
    return jsonify({'tasks':  map(__make_public_task, tasks)})    # 返回json

def __make_public_task(task):
    new_task = {}
    for field in task:
        if field == TASK_ID:
            new_task['uri'] = url_for('email.get_task', task_id=task[TASK_ID], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

'''
id ---> 发件箱,收件人等信息
for test:
curl -i -H "Content-Type: application/json" -X POST -d '{"content":"Read a book"}' http://localhost:5000/mail/task/1
'''
@emails.route('/task/<int:task_id>', methods=['POST'])
def mail_task(task_id):
    if not request.json:
        abort(400)
    task_file = None
    # 判断有无文件传输
    try:
        task_file = request.files[FILE]
        if len(task_file)>MAX_FILE_SIZE:
            return jsonify({'STATE': 'file oversize'}),FILE_OVERSIZE
    except Exception,e:
        logging.warn('none file')
    content = request.json[CONTENT]
    task = filter(lambda t: t[TASK_ID] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    # 构造消息json
    message = copy.deepcopy(task[0])
    message[MESSAGE_ID] = str(int(time.time()))
    message[FILE] = task_file
    message[CONTENT] = content

    # 持久化
    service.store_send_message(message=message)
    return jsonify({MESSAGE_ID: message[MESSAGE_ID],
                    TASK_ID:message[TASK_ID],
                    'STATE': 'success'}), 201



@emails.route('/task/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = filter(lambda t: t[TASK_ID] == task_id, tasks)
    if len(task) == 0:
        abort(404)  # 调用not_found函数
    return jsonify({'task': task[0]})


'''
Blueprint中注册程序全局的错误处理程序
'''
# @common.app_errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)

