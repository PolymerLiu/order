from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os

# 实现配置按需加载
# 定义一个Application类，继承自flask
class Application(Flask):
  def __init__(self,import_name,template_folder=None,static_folder=None):
    super(Application,self).__init__(import_name,template_folder=template_folder,static_folder=static_folder)
    # self 代指flask
    # 从指定文件夹加载文件
    self.config.from_pyfile('config/base_setting.py')

    if 'ops_config' in os.environ:
      self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])

    db.init_app(self)

db = SQLAlchemy()
# 重新指定相应的文件夹
app = Application(
  __name__,
  template_folder=os.getcwd()+'/web/templates/',
  static_folder=os.getcwd()+'/web/static/')

# 将app进行一次包装
manager = Manager(app)


# 函数模板
# 注入模板要用到的方法
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl,'buildUrl')
app.add_template_global(UrlManager.buildImageUrl,'buildImageUrl')