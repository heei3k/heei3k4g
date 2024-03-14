#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/12 15:22
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : email_manager.py
# @Software: PyCharm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManager:

    def send_email(self):
        smtpserver = "smtp.163.com"
        username = "heei3k@163.com"
        password = "MSPATQQJPGMBDJSC"

        receiver = ["lih@certusnet.com.cn", "heei3k@hotmail.com"]

        message = MIMEMultipart("related")
        subject = "bpm登录测试报告"

        # 附件
        attachment = MIMEText(open(r'D:\PycharmProjects\heei3k\allure-results\report.html', 'rb').read(), 'base64',
                              'utf-8')
        attachment["Content-Type"] = 'application/octet-stream'
        attachment.add_header("Content-Disposition", "attachment", filename=("gbk", "", "report.html"))

        message['From'] = username
        message['To'] = ",".join(receiver)
        message['Subject'] = subject
        message.attach(attachment)

        # 邮件正文
        text_plain = MIMEText(open(r'D:\PycharmProjects\heei3k\allure-results\report.html', 'rb').read(), 'html',
                              'utf-8')
        message.attach(text_plain)

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()


if __name__ == '__main__':
    EmailManager().send_email()
