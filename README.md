# SiomAutoLogin
所网自动登录

写这个主要原因是所网每天4点自动切断，需要重新登录。

之前的方法直接在http://1.1.1.2/ac_portal/login.php 中写入对应参数就可以

但是自从更新后密码变成了动态加密，还没有找到对应的加密算法，所以暂时这种方案先搁置

目前所用方案是利用selenium直接模拟浏览器的键盘输入和点击

# Log
306工作站的电脑不需要wifi连接，取消.bat文件中的wifi部分
