from flask import Blueprint,request
from application import app

route_api = Blueprint('api_page',__name__)

# 将API文件进行全量导入
from web.controllers.api.Member import *


@route_api.route('/')
def index():
  return 'mini api '