from flask import Flask
from imooc import route_imooc

app=Flask(__name__)

# 将Blueprint定义的路由注入到APP中
app.register_blueprint(route_imooc,url_prefix='/imooc')

@app.route("/")
def hello_world():
  return 'Hello World'

@app.route('/api')
def index():
  return 'index page'

@app.route('/api/hello')
def api_hello():
  return 'Hello World'

if __name__ == "__main__":
  app.run(host='0.0.0.0')

# service firewalld stop