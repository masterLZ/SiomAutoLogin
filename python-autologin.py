import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import time
from selenium import webdriver


def page_login(url):
    data = {
        "opr": "pwdLogin",
        "userName": "lizhan",
        "pwd": "bcac7bc4692c",
        "auth_tag": 1596421476152,
        "rememberPwd": "0"
    }
    r = requests.post(url, data=data)
    print(r.status_code)
    if r.status_code == 500:
        print('链接失败')
    else:
        print('链接成功')

def send_mail():
    # 第三方 SMTP 服务
    mail_host = "mail.cstnet.cn"  #设置服务器
    mail_user = "zhanli@siom.ac.cn"  #用户名
    mail_pass = "Lz406699313"  #口令

    sender = 'zhanli@siom.ac.cn'
    receivers = ['lizzzzz@mail.ustc.edu.cn']  # 接收邮箱

    message = MIMEText('306已连接', 'plain', 'utf-8')
    message['From'] = Header("306", 'utf-8')
    message['To'] = Header("李展", 'utf-8')

    subject = '自动运行报告'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, '25')  # 25 为默认端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

def SimulateClick(url):    
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    dr = webdriver.Firefox('./', options=options)
    dr.get(url)
    dr.find_element_by_id('password_name').send_keys('lizhan')
    dr.find_element_by_id('password_pwd').send_keys('080416')
    dr.find_element_by_name('btlogin').click()
    time.sleep(1)
    ResponseUrl = dr.current_url
    if ResponseUrl.find('ac_portal/default') > 0:
        print('Login Success')
    else:
        print('Login Num is limted')
        
    dr.quit()
    return ResponseUrl
    #  直接登录http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd&pop=0&type=logout&username=
    #  登录数量过多http://1.1.1.2/expire_term_default/expire_term.htm?url=http://1.1.1.2/ac_portal/proxy.html?type=logout&tabs=pwd


url = 'http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd'

ResponseUrl = SimulateClick(url)
send_mail()