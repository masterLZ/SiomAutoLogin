echo off
echo netsh wlan connect name=SIOM
echo %~dp0
%~d0
cd %~dp0
python.exe %~dp0login-4am.py
