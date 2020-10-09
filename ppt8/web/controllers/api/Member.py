from web.controllers.api import route_api
from flask import Blueprint,request,jsonify
from application import app

@route_api.route('/member/login',methods=['GET','POST'])
def login():
  resp = {'code':200,'msg':'操作成功','data':{}}
  req = request.values
  app.logger.info(req)
  return jsonify(resp)