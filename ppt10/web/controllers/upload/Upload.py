# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify
from application import app
import re,json
from common.libs.UploadService import UploadService

route_upload = Blueprint( 'upload_page',__name__ )

@route_upload.route( "/ueditor" ,methods=['GET','POST'])
def ueditor():

  req = request.values
  action = req['action'] if 'action' in req else ''
  # 加载配置文件
  if action == "config":
    root_path = app.root_path
    config_path = "{0}/web/static/plugins/ueditor/upload_config.json".format( root_path )
    with open( config_path,encoding="utf-8" ) as fp:
      try:
        config_data =  json.loads( re.sub( r'\/\*.*\*/' ,'',fp.read() ) )
      except:
        config_data = {}
    return  jsonify( config_data )
  # 上传图片
  if action == "uploadimage":
    return uploadImage()

  return 'testok'

def uploadImage():
  resp = {'state':'SUCCESS','url':'','title':'','original':''}
  file_target = request.files
  upfile = file_target['upfile'] if 'upfile' in file_target else None
  if upfile is None:
    resp['state'] = '上传失败'
    return jsonify(resp)
  
  ret = UploadService.uploadByFile(upfile)
  if ret['code'] != 200:
    resp['state'] = '上传失败' + ret['msg']
    return jsonify(resp)
  
  resp['url'] = ret['data']['file_key']




  return jsonify(resp)