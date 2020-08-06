CHCP 65001
echo off
<<<<<<< HEAD
echo 登陆中
python.exe .\python-autologin.py
=======
echo 连接wifi中
netsh wlan connect name=SIOM
echo 登录中
python.exe ./python_autologin.py
>>>>>>> f6d1f50e7cda98be18f13cf6b74ff899493c229f
pause