import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

import requests
from selenium import webdriver

from getRC4encod import get_rc4_psswd


def page_login():
    url = "http://1.1.1.2/ac_portal/login.php"
    name = "lizhan"
    password = "080416"
    pwd, auth_tag = get_rc4_psswd(password)
    data = {
        "opr": "pwdLogin",
        "userName": name,
        "pwd": pwd,
        "auth_tag": auth_tag,
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
    mail_host = "mail.cstnet.cn"  # 设置服务器
    mail_user = "zhanli@siom.ac.cn"  # 用户名
    mail_pass = "Lz406699313"  # 口令

    sender = 'zhanli@siom.ac.cn'
    receivers = ['lizzzzz@mail.ustc.edu.cn']  # 接收邮箱

    message = MIMEText('MSI网络已经重新链接', 'plain', 'utf-8')
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


<<<<<<< HEAD:python-autologin.py
def SimulateClick(url):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    dr = webdriver.Firefox(r'./', options=options)
=======
def SimulateClick(isFirst=1, driver=None):
    url = 'http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd'
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    dr = driver
    if (isFirst):
        dr = webdriver.Firefox('./')
>>>>>>> f6d1f50e7cda98be18f13cf6b74ff899493c229f:python_autologin.py
    dr.get(url)
    dr.implicitly_wait(30)
    dr.find_element_by_id('password_name').send_keys('lizhan')
    dr.find_element_by_id('password_pwd').send_keys('080416')
    # dr.find_element_by_name('btlogin').click()
    dr.find_element_by_id('password_submitBtn').click()
    # dr.implicitly_wait(30)
    time.sleep(3)
    ResponseUrl = dr.current_url
    if ResponseUrl.find('ac_portal/default') > 0:
        print('Login Success')
    else:
        print('Login Num is limted')
        #使用xpath筛选
        ip_uint = [
            dr.find_element_by_xpath('.//table/tbody/tr[3]/td[2]').text,
            dr.find_element_by_xpath('.//table/tbody/tr[4]/td[2]').text
        ]
        try:
            WorkstationIndex = ip_uint.index('172.16.43.50')
            print('306工作站在线，将删除另一个用户')
            DelteIndex = 1 - WorkstationIndex + 3
            #第三个或者第四个tr
        except ValueError:
            DelteIndex = 3
            print('删除第一个用户')
        XpathDelte = ".//table/tbody/tr[%d]/td[7]" % (DelteIndex)
        dr.find_element_by_xpath(XpathDelte).click()
        # 删除后重新调用登录
        print('重新登录')
        dr.switch_to_alert().accept()  #接受弹窗
        SimulateClick(0, dr)
    dr.quit()
    #  直接登录http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd&pop=0&type=logout&username=
    #  登录数量过多http://1.1.1.2/expire_term_default/expire_term.htm?url=http://1.1.1.2/ac_portal/proxy.html?type=logout&tabs=pwd


<<<<<<< HEAD:python-autologin.py
url = 'http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd'
ResponseUrl = SimulateClick(url)
send_mail()
=======
if __name__ == '__main__':
    SimulateClick()
    #page_login()
>>>>>>> f6d1f50e7cda98be18f13cf6b74ff899493c229f:python_autologin.py
