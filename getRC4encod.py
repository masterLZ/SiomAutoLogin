# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:30:50 2020

@author: LZ
"""
import execjs
def get_rc4_psswd(data):
    jsstr = get_js()
    ctx = execjs.compile(jsstr) #加载JS文件
    pwd_auth_tag = ctx.call('do_encrypt_rc4', data) #调用js方法  第一个参数是JS的方法名，后面的data是js方法的参数
    bu = pwd_auth_tag.split("||")
    pwd = bu[0]
    auth_tag = bu[1]
    return pwd,auth_tag 



def get_js():
    f = open("./rc4.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr


if __name__ == '__main__':
    pwd,auth_tag  = get_rc4_psswd('080416')
    print(pwd)
    print(auth_tag)
    