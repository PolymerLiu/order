参考文档
http://docs.jinkan.org/docs/flask/quickstart.html#a-minimal-application


# 防火墙操作
[参考文档] https://blog.csdn.net/u014722022/article/details/103838981

1.1 关闭防火墙：（不推荐，关闭防火墙毕竟不安全）

禁用： systemctl stop firewalld

查看状态： systemctl status firewalld

启动： systemctl start firewalld

停止（重启后依然关闭）： systemctl disable firewalld