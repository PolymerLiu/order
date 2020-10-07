# -*- coding: utf-8 -*-
from flask import Blueprint,request,redirect,jsonify
from common.libs.Helper import ops_render,iPagination,getCurrentDate
from common.models.User import User
from common.libs.UrlManager import UrlManager
from common.libs.user.UserService import UserService
from application import app,db

route_account = Blueprint( 'account_page',__name__ )

@route_account.route( "/index" )
def index():
    resp_data = {}
    query = User.query
    req = request.values

    page = int(req['page']) if ('page' in req and req['page']) else 1

    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': '/account/index'
    }
    pages = iPagination(page_params)
    # 想查询页码的第一条数据
    offset = (page - 1) * app.config['PAGE_SIZE']
    # 想查询页码的最后一条数据
    limit = app.config['PAGE_SIZE'] * page


    # 查询全量数据，并进行倒序排序
    list = query.order_by(User.uid.desc()).all()[offset:limit]
    resp_data['pages'] = pages
    resp_data['list'] = list
    return ops_render( "account/index.html",resp_data )

@route_account.route( "/info" )
def info():
    resp_data = {}
    req = request.args
    uid = int(req.get('id',0))
    reback_url = UrlManager.buildUrl('/account/index')
    if uid < 1:
        return redirect(reback_url)
    info = User.query.filter_by(uid=uid).first()
    if not info:
        return redirect(reback_url)
    resp_data['info'] = info

    return ops_render( "account/info.html",resp_data )

@route_account.route( "/set",methods=['GET','POST'] )
def set():
    default_pwd = '******'
    # 展示账户详情
    if request.method == 'GET':
        resp_data = {}
        req = request.args
        uid = int(req.get('id',0))
        user_info = None
        if uid :
            user_info = User.query.filter_by(uid=uid).first()
        resp_data['user_info'] = user_info
        return ops_render( "account/set.html",resp_data )
    
    # 新建账户
    req = request.values
    resp = {'code':200,'msg':'操作成功','data':{}}

    id = req['id'] if 'id' in req else ''
    nickname = req['nickname'] if 'nickname' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    email = req['email'] if 'email' in req else ''
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的姓名~~'
        return jsonify(resp)

    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的手机号码~~'
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的邮箱~~'
        return jsonify(resp)

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的登录用户名~~'
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的登录密码~~'
        return jsonify(resp)
    # 如果新增用户，只需判断新增的用户名和数据库用户名是否相等即可
    # 如果是修改用户，需要判断除当前用户外还有没有相同的用户名
    # filter方法可以传入多个参数进行判断
    has_in = User.query.filter(User.login_name == login_name,User.uid != id).first()
    
    if has_in:
        resp['code'] = -1
        resp['msg'] = '该登录名已经存在，请换一个试试~~'
        return jsonify(resp)

    user_info = User.query.filter_by(uid = id).first()

    # 修改用户信息
    if user_info:
        model_user = user_info
    # 新增加用户
    else:
        model_user = User()
        model_user.login_salt = UserService.geneSalt()
        model_user.created_time = getCurrentDate()

    model_user.nickname = nickname
    model_user.mobile = mobile
    model_user.email = email
    model_user.login_name = login_name
    model_user.update_time = getCurrentDate()
    if login_pwd != default_pwd:
        model_user.login_pwd = UserService.genePwd(login_pwd,model_user.login_salt)
        

    db.session.add(model_user)
    db.session.commit()

    return jsonify(resp)

