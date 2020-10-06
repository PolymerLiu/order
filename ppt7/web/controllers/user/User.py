# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,jsonify
from common.models.User import User
from common.libs.user.UserService import UserService

route_user = Blueprint( 'user_page',__name__ )

@route_user.route( "/login",methods = ['GET','POST'] )
def login():
    if request.method=='GET':
        return render_template( "user/login.html" )

    resp = {'code':200,'msg':'登录成功','data':{}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的登录用户名~~'
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的登录密码~~'
        return jsonify(resp)
    
    
    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和登录密码~~1'
        return jsonify(resp)

    if user_info.login_pwd != UserService.genePwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和登录密码~~2'
        return jsonify(resp)
    return jsonify(resp)

@route_user.route( "/edit" )
def edit():
    return render_template( "user/edit.html" )

@route_user.route( "/reset-pwd" )
def resetPwd():
    return render_template( "user/reset_pwd.html" )