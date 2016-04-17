# SrunIsShit
A python desktop program to restart Srun client instantly once it has crashed. 用于立即重启崩溃的深澜客户端。

## 说明：

1. 本程序仅适用于win32平台
2. 本程序Python版本为2.7
3. 使用时请首先修改客户端路径与测试用的网站URL，随后使用cx_Freeze打包成可执行文件

## 背景：

由于我校校园网认证系统于2014年时更换为深澜系统后，这个深澜客户端在我的笔记本上经常无故闪退造成断网。当时比较忙没时间具体做个发心跳包的第三方客户端也不想重装系统解决，索性就用Python随手写了个能在网络断开后自动重启深澜客户端的小工具。今天整理硬盘恰好发现了这个小工具，就push到Github上以方便有需要的朋友。

## License：

MIT License