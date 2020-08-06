CHCP 65001
echo off
echo 连接wifi中
netsh wlan connect name=SIOM
echo 登录中
python.exe ./python_autologin.py
pause

