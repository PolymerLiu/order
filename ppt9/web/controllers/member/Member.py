# -*- coding: utf-8 -*-
from flask import Blueprint,request,redirect,jsonify
from common.libs.Helper import ops_render,iPagination,getCurrentDate
from common.libs.UrlManager import UrlManager
from common.models.member.Member import Member
from application import app,db

route_member = Blueprint( 'member_page',__name__ )

@route_member.route( "/index" )
def index():
    resp_data = {}
    query = Member.query
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1

    if 'status'in req and int(req['status'])>-1:
        query = query.filter(Member.status == int(req['status']))

    if 'mix_kw'in req :
        query = query.filter(Member.nickname.ilike('%{0}%'.format(req['mix_kw'])))

    page_params = {
        'total':query.count(),
        'page_size':app.config['PAGE_SIZE'],
        'display':app.config['PAGE_DISPLAY'],
        'page':page,
        'url':request.full_path.replace('&p={}'.format(page),'')
    }

    pages = iPagination(page_params)
    offset = (page - 1)*app.config['PAGE_SIZE']
    # Member.id.desc(),根据ID进行倒序排序
    # offset(offset).limit(size),从offset开始偏移size个结果
    list = query.order_by(Member.id.desc()).offset(offset).limit(app.config['PAGE_SIZE']).all()
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    resp_data['current'] = 'index'

    return ops_render( "member/index.html",resp_data )

@route_member.route( "/info" )
def info():
    resp_data = {}
    req = request.args
    id = int(req.get('id',0))
    if id <1 :
        return redirect(UrlManager.buildUrl('/member/index'))

    info = Member.query.filter_by(id=id).first()
    resp_data['current'] = 'index'
    resp_data['info'] = info

    return ops_render( "member/info.html",resp_data )

@route_member.route( "/set",methods=['POST','GET'] )
def set():
    # 展示账户详情
    if request.method == 'GET':
        resp_data = {}
        req = request.args
        id = int(req.get('id',0))
        reback_url = UrlManager.buildUrl('/member/index')
        if id < 1:
            return redirect(reback_url)
        info = Member.query.filter_by(id=id).first()
        if not info:
            return redirect(reback_url)
        resp_data['info'] = info
        resp_data['current'] = 'index'
        return ops_render( "member/set.html",resp_data )

    # 修改用户名
    req = request.values
    resp = {'code':200,'msg':'操作成功','data':{}}

    id = req['id'] if 'id' in req else ''
    nickname = req['nickname'] if 'nickname' in req else ''
    if nickname is None or len(nickname)<1 :
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的姓名~~'
        return jsonify(resp)

    member_info = Member.query.filter_by(id=id).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = '指定会员不存在~~'
        return jsonify(resp)

    member_info.nickname = nickname
    member_info.update_time = getCurrentDate()

    db.session.add(member_info)
    db.session.commit()

    return jsonify(resp)
    
    

@route_member.route( "/comment" )
def comment():
    return ops_render( "member/comment.html" )
