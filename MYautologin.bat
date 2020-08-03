CHCP 65001
echo off
echo 连接wifi中
netsh wlan connect name=SIOM
echo ...
python.exe ./python-autologin.py
pause