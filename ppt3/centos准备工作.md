# 配置好IP，使
查看IP
ip addr
ifconfig // command not found

vi /etc/resolv.conf   (添加 nameserver 114.114.114.114)
vi /etc/sysconfig/network-scripts/ifcfg-xx

service network restart


yum update

ping www.baidu.com  ping 不通
yum install net-tools // 虚拟主机无法上网还不能进行安装



virtualbox 网络选择桥接网卡，虚拟主机获得IP

通过SSH远程连接

ssh root@192.168.1.8


# 替换默认源
http://mirrors.163.com/.help/centos.html

首先备份/etc/yum.repos.d/CentOS-Base.repo
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

下载对应版本repo文件, 放入/etc/yum.repos.d/
cd /etc/yum.repos.d/
curl http://mirrors.163.com/.help/CentOS7-Base-163.repo -o CentOS7-Base-163.repo

运行以下命令生成缓存
yum clean all
yum makecache

yum install wget


# 安装vim ： 
cd /
yum install vim

