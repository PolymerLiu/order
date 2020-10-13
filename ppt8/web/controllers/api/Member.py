from flask import Blueprint,request,jsonify
from application import app,db
import requests,json
from web.controllers.api import route_api
from common.models.member.Member import Member
from common.models.member.OauthMemberBind import OauthMemberBind
from common.libs.Helper import getCurrentDate

@route_api.route('/member/login',methods=['GET','POST'])
def login():
  resp = {'code':200,'msg':'操作成功','data':{}}
  req = request.values
  code = req['code'] if 'code' in req else ''
  if not code or len(code) < 1:
    resp['code'] = -1
    resp['msg'] = '需要code'
    return jsonify(resp)
  
  url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code".format(app.config['MINA_APP']['appid'],app.config['MINA_APP']['appkey'],code)
  r = requests.get(url)
  res = json.loads(r.text)
  openid = res['openid']

  nickname = req['nickName'] if 'nickName' in req else ''
  sex = req['gender'] if 'gender' in req else ''
  avatar = req['avatarUrl'] if 'avatarUrl' in req else ''

  # 判断是否已经绑定过，如果已经绑定则直接返回一些信息
  bind_info = OauthMemberBind.query.filter_by(openid=openid,type=1).first()
  if not bind_info:
    model_member = Member()
    model_member.nickname = nickname
    model_member.sex = sex
    model_member.avatar = avatar
    model_member.reg_ip = ''
    model_member.salt = ''
    model_member.updated_time = model_member.updated_time = getCurrentDate()
    db.session.add(model_member)
    db.session.commit()

    model_bind = OauthMemberBind()
    model_bind.member_id = model_member.id
    model_bind.type = 1
    model_bind.client_type = 'weixin'
    model_bind.openid = openid
    model_bind.updated_time = model_bind.updated_time = getCurrentDate()
    model_bind.extra = ''
    db.session.add(model_bind)
    db.session.commit()

    bind_info = model_bind

  member_info = Member.query.filter_by(id=bind_info.member_id).first()
  resp['data'] = {'nickname':member_info.nickname}
  return jsonify(resp)