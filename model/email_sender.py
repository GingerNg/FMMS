#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: email_sender.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-4 下午9:13
 @desc: test email
"""
import sys
from email.mime.multipart import MIMEMultipart

reload(sys)
sys.setdefaultencoding('utf8')


import smtplib
from email.mime.text import MIMEText
import premailer
from utils.constants import *
from sender import Sender

content_template = premailer.transform(
    """
             <html>
             <style type="text/css">
             h1 { border:1px solid black }
             p { color:red;}
             p::first-letter { float:left; }
             </style>
             <p>%s</p>
             </html>
     """
)


class EmailSender(Sender):
    def __init__(self,host, username, passwd,mail_type,sender_id):
        self.__host = host
        self.__username = username
        self.__passwd = passwd
        self.__mail_type = mail_type
        self.__sender_id = sender_id

    def send_message(self,message):
        send_to = message[RECEIVERS]
        subject = message[SUBJECT]
        content = message[CONTENT]
        self.send(send_to=send_to,subject=subject,content=content)


    def send(self,send_to, subject, content):
        # msg = MIMEText(content.encode('utf-8'), _subtype='html', _charset='utf-8')
        msg = MIMEMultipart()
        msg.attach(MIMEText(content_template %(content), 'html'))
        msg['From'] = self.__username
        msg['Subject'] = u'%s' % subject
        msg['To'] = ",".join(send_to)

        try:
            s = smtplib.SMTP_SSL(self.__host, 465)
            s.login(self.__username, self.__passwd)
            s.sendmail(self.__username, send_to, msg.as_string())
            s.close()
            print "邮件发送成功"
        except Exception as e:
            print 'Exception: send email failed', e

def send_email(host, username, passwd, send_to, subject, content):
    # msg = MIMEText(content.encode('utf-8'), _subtype='html', _charset='utf-8')
    msg = MIMEMultipart()
    msg.attach(MIMEText(content, 'html'))
    msg['From'] = username
    msg['Subject'] = u'%s' % subject
    msg['To'] = ",".join(send_to)

    try:
        s = smtplib.SMTP_SSL(host, 465)
        s.login(username, passwd)
        s.sendmail(username, send_to, msg.as_string())
        s.close()
        print "邮件发送成功"
    except Exception as e:
        print 'Exception: send email failed', e


if __name__ == '__main__':
    pass



    # send_email(host, username, passwd, to_list, subject, content)
