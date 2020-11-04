import hashlib,base64,random,string
from application import app,db
import requests,json
from common.libs.Helper import getCurrentDate
from common.models.member.MemberCart import MemberCart

class CartService:

  @staticmethod
  def setItems(member_id=0,food_id=0,number=0):
    if member_id < 1 or food_id < 1 or number < 1 :
      return False

    # 购物车商品，用户已经添加此商品，变更数量。否则新增此商品
    cart_info = MemberCart.query.filter_by(food_id=food_id,member_id=member_id).first()
    if cart_info:
      model_cart = cart_info
    else:
      model_cart = MemberCart()
      model_cart.member_id = member_id
      model_cart.created_time = getCurrentDate()

    model_cart.food_id = food_id
    model_cart.quantity = number
    model_cart.updated_time = getCurrentDate()
    db.session.add(model_cart)
    db.session.commit()
    return True
    