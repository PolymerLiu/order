Python Flask订餐系统

## 进入到对应环境和目录
激活对应虚拟环境
source imooc/bin/activate
进入到源码文件夹
cd /home/www

## 启动
export ops_config=local 
python manager.py runserver

查看某个端口的使用情况
netstat -tunlp |grep 8000

杀死某个端口
kill pid
