CHCP 65001
echo off
echo 连接wifi中
netsh wlan connect name=SIOM
echo ...
python.exe D:/MyCoding/自动登录/python-autologin.py
pause