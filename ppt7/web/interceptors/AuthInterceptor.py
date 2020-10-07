from application import app
from flask import request,redirect,g
from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
import re

# 在请求到达controller之前，先经过before_request
@app.before_request
def before_request():
  ignore_urls = app.config['IGNORE_URLS']
  ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
  path = request.path

  # 如果是静态资源及其他资源，则不需要授权校验
  pattern = re.compile('%s' % '|'.join(ignore_check_login_urls))
  if pattern.match(path):
    return

  # 检查用户是否已经登录，如果登录则返回对应的用户信息
  user_info = check_login()
  # 将用户信息赋值给g.current_user
  g.current_user = None
  if user_info:
    g.current_user = user_info

  # 如果是登录页面，也不需要授权校验
  pattern = re.compile('%s' % '|'.join(ignore_urls))
  if pattern.match(path):
    return

  if not user_info:
    return redirect(UrlManager.buildUrl('/user/login'))

  return

# 判断用户是否已经登录
def check_login():
  cookies = request.cookies
  auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None

  # 校验cookie
  # 根据cookie里存储的uid,查到对应的用户信息，再用用户信息去生成一个授权码和用户传过来的授权码进行对比
  if auth_cookie is None:
    return False
  
  auth_info = auth_cookie.split('#')
  if len(auth_info) != 2 :
    return False
  
  try:
    user_info = User.query.filter_by(uid=auth_info[1]).first()
  except Exception:
    return False

  if user_info is None:
    return False
  
  if auth_info[0] != UserService.geneAuthCode(user_info):
    return False

  return user_info
