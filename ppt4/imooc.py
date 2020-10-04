from flask import Blueprint

# 定义路由变量
route_imooc = Blueprint('imooc_page',__name__)

@route_imooc.route('/')
def index():
  return 'imooc index page'

@route_imooc.route('/api')
def api():
  return 'imooc api page'