# -*- coding: utf-8 -*-
from flask import Blueprint,request
from common.libs.Helper import ops_render,iPagination
from common.models.User import User
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
    return ops_render( "account/info.html" )

@route_account.route( "/set" )
def set():
    return ops_render( "account/set.html" )
