# 参考文档
flask 
http://docs.jinkan.org/docs/flask/quickstart.html#a-minimal-application

flask-sqlalchemy
http://www.pythondoc.com/flask-sqlalchemy/quickstart.html
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application


4.8数据库ORM
pip install flask-sqlalchemy

yum -y install mysql-devel gcc gcc-devel python-devel

pip install mysqlclient


# 防火墙操作
[参考文档] https://blog.csdn.net/u014722022/article/details/103838981

1.1 关闭防火墙：（不推荐，关闭防火墙毕竟不安全）

禁用： systemctl stop firewalld

查看状态： systemctl status firewalld

启动： systemctl start firewalld

停止（重启后依然关闭）： systemctl disable firewalld