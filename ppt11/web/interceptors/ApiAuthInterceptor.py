from application import app
from flask import request,redirect,g,jsonify
from common.models.member.Member import Member
from common.libs.member.MemberService import MemberService
from common.libs.UrlManager import UrlManager
from common.libs.LogService import LogService
import re

# API认证
# 在请求到达controller之前，先经过before_request
@app.before_request
def before_request():
  api_ignore_urls = app.config['API_IGNORE_URLS']
  path = request.path
  if '/api' not in path:
    return False

  # 检查用户是否已经登录，如果登录则返回对应的用户信息
  member_info = check_member_login()
  # 将用户信息赋值给g.current_user
  g.current_user = None
  if member_info:
    g.current_user = member_info

  pattern = re.compile('%s' % '|'.join(api_ignore_urls))
  if pattern.match(path):
    return

  if not member_info:
    resp = {'code':-1,'msg':'未登录','data':{}}
    return jsonify(resp)

  return

# 判断用户是否已经登录
def check_member_login():
  auth_cookie = request.headers.get('Authorization')

  if auth_cookie is None:
    return False
  
  auth_info = auth_cookie.split('#')
  if len(auth_info) != 2 :
    return False
  
  try:
    member_info = Member.query.filter_by(id=auth_info[1]).first()
  except Exception:
    return False

  if member_info is None:
    return False
  
  if auth_info[0] != MemberService.geneAuthCode(member_info):
    return False
  # 非正常状态的账号，应该禁止其任何操作
  if member_info.status != 1:
    return False

  return member_info
