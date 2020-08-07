import time

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


def SimulateClick(isFirst=1, driver=None):
    url = 'http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd'
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    dr = driver
    if (isFirst):
        dr = webdriver.Firefox('./')
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

        DelteIndex = 3
        print('删除第一个用户')
        XpathDelte = ".//table/tbody/tr[%d]/td[7]" % (DelteIndex)
        dr.find_element_by_xpath(XpathDelte).click()
        # 删除后重新调用登录
        print('重新登录')
        dr.switch_to.alert.accept()  #接受弹窗
        SimulateClick(0, dr)
    dr.quit()
    #  直接登录http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd&pop=0&type=logout&username=
    #  登录数量过多http://1.1.1.2/expire_term_default/expire_term.htm?url=http://1.1.1.2/ac_portal/proxy.html?type=logout&tabs=pwd


if __name__ == '__main__':
    SimulateClick()
