from flask import Flask,url_for
from imooc import route_imooc
from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# 将Blueprint定义的路由注入到APP中
app.register_blueprint(route_imooc,url_prefix='/imooc')

# 配置连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/mysql'
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
  url = url_for('index')
  url_1 = UrlManager.buildUrl('/api')
  url_2 = UrlManager.buildStaticUrl('/css/bootstrap.css')

  msg = 'Hello World,url:%s,url_1:%s,url_2:%s'%(url,url_1,url_2)

  app.logger.info(msg)
  app.logger.error(msg)

  return msg

@app.route('/api')
def index():
  return 'index page'

@app.route('/api/hello')
def api_hello():

  from sqlalchemy import text
  sql = text('select * from `user`')
  # 执行sql语句
  result = db.engine.execute(sql)
  for row in result:
    app.logger.info(row)

  return 'Hello World'

@app.errorhandler(404)
def page_not_found(error):
  app.logger.error(error)
  return 'This page does not exist', 404

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

# service firewalld stop