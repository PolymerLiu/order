from werkzeug.utils import secure_filename
from application import app
from common.libs.Helper import getCurrentDate
import os,stat,uuid

class UploadService:
  @staticmethod
  def uploadByFile(file):
    config_upload = app.config['UPLOAD']
    resp = {'code':200,'msg':'操作成功~~','data':{}}
    # 获取文件名
    filename = secure_filename(file.filename)
    # 获取文件拓展类型
    ext = filename.rsplit('.',1)[1]
    if ext not in config_upload['ext']:
      resp['code'] = -1
      resp['msg'] = '不允许的拓展类型文件'
      return resp

    root_path = app.root_path + config_upload['prefix_path']
    file_dir = getCurrentDate('%Y%m%d')
    save_dir = root_path + file_dir
    if not os.path.exists(save_dir):
      os.mkdir(save_dir)
      os.chmod(save_dir,stat.S_IRWXU | stat.S_IRGRP | stat.S_IRWXO)

    filename = str(uuid.uuid4()).replace('-','') + '.' + ext
    file.save('{0}/{1}'.format(save_dir,filename))

    resp['data'] = {
      'file_key': file_dir + '/' + filename
    }
    return resp