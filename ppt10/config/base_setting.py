# 公用的配置

SERVER_PORT = 8000
DEBUG = False
SQLALCHEMY_ECHO = False

AUTH_COOKIE_NAME = 'mooc_food'

# 过滤URL
IGNORE_URLS = [
  '^/user/login',
  # 对所有API接口都不做登录校验
  '^/api',
]

IGNORE_CHECK_LOGIN_URLS = [
  '^/static',
  '^/favicon.ico',
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
  '1': '正常',
  '0': '已删除'
}

MINA_APP = {
  'appid': 'wx011f61b888b43a34',
  'appkey': '692e3304376d7111e399a4ef6573bba3',
}

UPLOAD = {
  'ext': ['jpg','jpeg','png','gif','bmp'],
  'prefix_path':'/web/static/upload/',
  'prefix_url':'/static/upload',
}