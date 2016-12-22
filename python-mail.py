#coding=utf8
#对test01,test10,test111类似字母加数字的组合字符串按照指定字符后面的数字大小进行排序
def Testsort(TestList,zifu):
    TestList.sort()
    def shanchu(s):
        return s[0:len(zifu)]==zifu
    TestList=filter(shanchu,TestList)

    if len(TestList) != 0:
        a=len(TestList)
        aa=[]
        for i in range(0,a):
            aaa=int(TestList[i][len(zifu):])
            aa.append(aaa)
        # print aa
        a1=zip(aa,TestList)
        a1.sort()
        TestList1=[]
        for i in range(0,a):
            TestList1.append(a1[i][1])
    return TestList1

a=["config","test1","tets10","test23","test14","shit",'test100000000',"LAS-1","LAS-23","LAS-2","LAS-55"]
print(Testsort(a,"LAS-"))

# -*- coding: UTF-8 -*-
#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
# mailsend(发件人工号，登陆密码，收件人，主题，内容，标题)
def mailsend(mail_user,mail_pass,receivers,subject,str1,project_name="Accelink--Test Dep.",):
    mail_host='smtp.accelink.com'  #设置服务器
    mail_user="%s@accelink.com"%(mail_user)    #用户名
    # mail_pass="Qcj19921023"   #口令

    sender = mail_user
    # receivers = ['237055098@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(str1, 'plain', 'utf-8')
    message['From'] = Header(project_name, 'utf-8')
    message['To'] =  Header("测试工程师", 'utf-8')

    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)    # 25为SMTP端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    finally:
        smtpObj.close()
