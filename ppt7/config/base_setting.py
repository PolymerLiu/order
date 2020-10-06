# 公用的配置

SERVER_PORT = 8000
DEBUG = False
SQLALCHEMY_ECHO = False

AUTH_COOKIE_NAME = 'mooc_food'

# 过滤URL
IGNORE_URLS = [
  '^/user/login'
]

IGNORE_CHECK_LOGIN_URLS = [
  '^/static',
  '^/favicon.ico',
]
