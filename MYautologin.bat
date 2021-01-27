@echo off
CHCP 65001
echo 连接wifi中
echo netsh wlan connect name=SIOM
echo 登录中
python.exe %~dp0/python_autologin.py


