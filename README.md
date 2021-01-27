# SiomAutoLogin
所网自动登录

登录方式有两种：网页直接发送请求和模拟浏览器操作

# 网页直接发送请求

所网直接登录，直接向 http://210.72.9.2/homepage/login.php 发送请求

目前请求包的内容是：{
        "opr": "login",
        "userName": name,
        "pwd": pwd,
        "auth_tag": auth_tag,
        "rememberPwd": "0"}

其中pwd 和 auth_tag 参数需要通过调用 rc4.js 对原本密码进行加密

pwd是加密后的密码, auth_tag是获取的系统时间毫秒数

该方法需要python库 requests, execjs

方法较为快捷，但是不够灵活，适用于每天4点登录

使用方法： 在计划任务中添加每天4：01分执行loginAt4am.bat

需要注意 在编辑“操作”选项卡时，找到“起始于（可选）”： 填入程序所在目录，比如：E:\Tools\  

# 调用浏览器模拟输入

通过selenium和浏览器对应版本的driver完成操作（Firefox 79.0+ geckodriver.exe）

登陆网址改为

主要功能是如果模拟登录后已经有两个在线的地址，则判断IP地址是否有工作站IP，如果有则删除另外一个，如果没有则删除第一个地址，然后再重新登录

该方法需要python库 selenium

缺点是速度很慢，打开浏览器需要一定时间，适用于日常自主登录

使用方法： 在计划任务中添加每天4：01分执行MYautologin.bat

需要注意 在编辑“操作”选项卡时，找到“起始于（可选）”： 填入程序所在目录，比如：E:\Tools\  

如果使用IE浏览器首先保证下载的浏览器驱动与selenium的版本号一致，另外如果文本框输入过慢需要把64位驱动换成32位

# 使用powershell登录

利用powershell 调用 IE浏览器完成登录，这个方法适用于任何windows电脑

# Log
2020/8/3 修改检索路径

2020/8/6 解决登录问题

2021/1/27 所网更改了入口和界面参数，所以重新更新。
