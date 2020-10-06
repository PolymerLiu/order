# 后台管理员模块功能
0：新建数据库
	数据库名：food_db
	CREATE DATABASE `food_db` DEFAULT CHARACTER SET = `utf8mb4`;
1：新建管理员数据表
	课程文件 文件夹中  数据库文件  文件夹 有初始化的所有SQL
2：使用 flask-sqlacodegen 扩展 方便快速生成 ORM model
	2.1 pip install flask-sqlacodegen
	2.2 使用方法
  <!-- 对food_db下的所有的表生成model -->
	flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
  <!-- 对food_db下的user表生成model -->
  flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/User.py"  --flask

3： 修改自动生成的model中的db变量

	from application import db

4：修改配置文件
	
	SQLALCHEMY_DATABASE_URI = 'mysql://root:对应root的密码@127.0.0.1/food_db'



# 请将下面的SQL语句执行，然后默认登录账号是root 密码是123456

INSERT INTO `user` (`uid`, `nickname`, `mobile`, `email`, `sex`, `avatar`, `login_name`, `login_pwd`, `login_salt`, `status`, `updated_time`, `created_time`)
VALUES
	(1, '编程浪子www.54php.cn', '11012345679', 'apanly@163.com', 1, '', 'root', '816440c40b7a9d55ff9eb7b20760862c', 'cF3JfH5FJfQ8B2Ba', 1, '2017-03-15 14:08:48', '2017-03-15 14:08:48');

查询表数据
select * from user \G;	
