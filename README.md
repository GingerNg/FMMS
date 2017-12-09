# FMSS
**Flask-based Message Sender Service**
###module:
- email
- 

#####结构:
- configer--daemon(views)--request--service--model--dao

- **java-style**

####命名说明:
- 文件,模块---小写(尽量单个单词) 单词之间用_分割 
- class--单词首字母大写
- 普通变量-- 小写,单词之间以下划线连接,私有前缀__
- 实例变量： 
以_开头，其他和普通变量一样 
- 函数-- 小写,单词之间以下划线连接,私有前缀__
- 全局变量名（类变量，在java中相当于static变量）： 
大写字母，单词之间用_分割
 

####restful api


####usage
- start service: python daemon.py 

##install:
####### MongoDB

    pip install pymongo
    
    
## TODO:
- logging  location
- db
- conf yml
- async
- frontend
- failover retry  --  zookeeper?

switch from pycharm to vscode

- reference: 
https://github.com/thieman/dagobah


- This is the Flask website.
- http://flask.pocoo.org/