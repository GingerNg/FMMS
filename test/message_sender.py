#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: message_sender.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-25 下午9:11
 @desc: 
"""
import json
import requests
from urlparse import urljoin
'''
python requests 调用restful api
'''

class MessageSender():
    def __init__(self, url, resource_pos=None):
        self.__url = url
        self.__resource_pos = resource_pos

    def __composite_target_url(self, resource_pos):
        if resource_pos is None:
            target_url = urljoin(self.__url, self.__resource_pos)
        else:
            # target_url = urljoin(self.__url, resource_pos)
            target_url =self.__url + resource_pos
        return target_url

    def message_send(self, data, resource_pos=None):
        headers = {"Content-Type": "application/json"}
        target_url = self.__composite_target_url(resource_pos)
        data_json = json.dumps(data)
        result = requests.post(target_url, headers=headers, data=data_json)
        return result

    def message_multipart_post(self,file_path,resource_pos = None):
        target_url = self.__composite_target_url(resource_pos)
        files = {'file': open(file_path, 'rb')}
        return requests.post(target_url,files=files).text

    def message_get(self, resource_pos):
        target_url = urljoin(self.__url, resource_pos)
        return requests.get(target_url).text

    def message_put(self, data, resource_pos):
        headers = {"Content-Type": "application/json"}  # 必需
        target_url = self.__composite_target_url(resource_pos)
        data_json = json.dumps(data)
        return requests.put(target_url, headers=headers, data=data_json).text

    def message_delete(self, resource_pos):
        headers = {"Content-Type": "application/json"}  # 必需
        target_url = urljoin(self.__url, resource_pos)
        data_json = json.dumps(data)
        return requests.delete(target_url, headers=headers, data=data_json).text

if __name__ == '__main__':
    # post test
    root_url = 'http://10.101.9.67:5000'

    resource_pos = '/todo/api/v1.0/tasks'

    resource_pos1 = '/mail_task'

    resource_pos2 = '/mail_result_task'

    resource_pos3 = '/fortest'

    print type(resource_pos3)

    data = {"title": "copy a book"}

    msg_sender = MessageSender(root_url)

    msg_sender.message_put(data, resource_pos3)

    # print open('result.txt', 'rb')
    # print message_send(root_url, resource_pos1, data)    # <Response [201]>
    # print msg_sender.message_multipart_post(file_path='result.txt',resource_pos=resource_pos2)
    # get test
    # print message_get(root_url,resource_pos=resource_pos)

    # put test
    # data = {"done":False}
    # print message_put(root_url, resource_pos)

