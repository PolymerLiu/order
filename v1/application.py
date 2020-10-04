from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

# 实现配置按需加载
# 定义一个Application类，继承自flask
class Application(Flask):
  def __init__(self,import_name):
    super(Application,self).__init__(import_name)
    # self 代指flask
    # 从指定文件夹加载文件
    self.config.from_pyfile('config/base_setting.py')


    db.init_app(self)

db = SQLAlchemy()
app = Application(__name__)

# 将app进行一次包装
manager = Manager(app)