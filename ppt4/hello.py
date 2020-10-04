from flask import Flask,url_for
from imooc import route_imooc
from common.libs.UrlManager import UrlManager

app=Flask(__name__)

# 将Blueprint定义的路由注入到APP中
app.register_blueprint(route_imooc,url_prefix='/imooc')

@app.route("/")
def hello_world():
  url = url_for('index')
  url_1 = UrlManager.buildUrl('/api')
  url_2 = UrlManager.buildStaticUrl('/css/bootstrap.css')
  return 'Hello World,url:%s,url_1:%s,url_2:%s'%(url,url_1,url_2)

@app.route('/api')
def index():
  return 'index page'

@app.route('/api/hello')
def api_hello():
  return 'Hello World'

if __name__ == "__main__":
  app.run(host='0.0.0.0')

# service firewalld stop