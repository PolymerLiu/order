from flask import Blueprint,request,jsonify
from application import app,db
import requests,json
from web.controllers.api import route_api
from common.libs.Helper import getCurrentDate
from common.models.food.FoodCat import FoodCat
from common.models.food.Food import Food
from common.libs.UrlManager import UrlManager

@route_api.route('/food')
def test():
  return 'test'


@route_api.route('/food/index')
def foodIndex():
  resp = {'code':200,'msg':'操作成功~','data':{}}
  cat_list = FoodCat.query.filter_by(status = 1).order_by(FoodCat.weight.desc()).all()
  # 组装类目列表
  data_cat_list = []
  data_cat_list.append({
    'id':0,
    'name':'全部'
  })
  if cat_list:
    for item in cat_list:
      tmp_data = {
        'id':item.id,
        'name':item.name
      }
      data_cat_list.append(tmp_data)
  # 查询正常状态的销量最好的食物倒序排列
  food_list = Food.query.filter_by(status = 1).order_by(Food.total_count.desc(),Food.id.desc()).limit(3).all()
  data_food_list = []

  if food_list:
    for item in food_list:
      tmp_data = {
        'id':item.id,
        'pic_url': UrlManager.buildImageUrl(item.main_image)
      }
      data_food_list.append(tmp_data)

  resp['data']['cat_list'] = data_cat_list
  resp['data']['banner_list'] = data_food_list
  return jsonify(resp)

@route_api.route('/food/search')
def foodSearch():
  return
