# -*- coding: utf-8 -*-
# @Time    : 2019/3/29/029 20:55
# @Author  : bing
# @File    : email_report.py
# @Software: PyCharm

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header


class email_Smtp:
    '''
    smtp-emai; sendmail
    '''
    def __init__(self,email_User,email_Pwd,to_Email_user):
        self.email_User = email_User
        self.to_Email_user = to_Email_user
        self.server = smtplib.SMTP_SSL("smtp.qq.com",465)
        self.server.login(email_User,email_Pwd)

    def send_email_msg(self,file_path):
        test_Time = str(time.strftime("%Y_%m_%d",time.localtime()))
        test_file_name = test_Time + "_testCase_request_Report.HTML"
        msg_total = MIMEMultipart()  # multipart类型主要有三种子类型；mixed、alternative、related 默认mixed
        msg_total['From'] = Header("Test-Mine",'utf-8')
        msg_total['To'] = Header("leader",'utf-8')
        msg_total['Subject'] = '测试报告'
        # 正文模块
        msg_raw = open(file_path,"r",encoding='utf-8').read()
        msg = MIMEText(msg_raw,'html')
        msg_total.attach(msg)
        # 附件模块
        mfile = MIMEApplication(open(file_path,"rb").read())
        # 添加附件的头信息
        mfile.add_header("Content-Disposition","attachment",filename=test_file_name)
        # 添加附件模块
        msg_total.attach(mfile)
        self.server.sendmail(self.email_User, self.to_Email_user, msg_total.as_string())
        print("邮件发送成功！请查收")

    def send_email_msgExcel(self,file_path,txt):
        test_Time = str(time.strftime("%Y_%m_%d",time.localtime()))
        test_file_name = test_Time + "_cases.xlsx"
        msg_total = MIMEMultipart()
        msg = MIMEText(txt,'plain','utf-8')
        msg_total.attach(msg)
        msg_total['From'] = Header("Test-Mine",'utf-8')
        msg_total['To'] = Header("leader",'utf-8')
        msg_total['Subject'] = '测试报告'
        # 附件模块
        mfile = MIMEApplication(open(file_path,"rb").read())
        # 添加附件的头信息
        mfile.add_header('Content-Disposition','attachment',filename=test_file_name)
        # 添加附件模块
        msg_total.attach(mfile)
        self.server.sendmail(self.email_User,self.to_Email_user,msg_total.as_string())
        print("邮件发送成功！请查收")

    def send_email_text(self,txt):
        msg_total = MIMEText(txt,'plain','utf-8')
        msg_total['From'] = Header("Test-Mine",'utf-8')
        msg_total['To'] = Header("leader",'utf-8')
        msg_total['Subject'] = '测试报告'
        self.server.sendmail(self.email_User,self.to_Email_user,msg_total.as_string())
        print("邮件发送成功！请查收")


