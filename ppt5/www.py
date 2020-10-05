from application import app
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.account.Account import route_account

# 每次增加新的模块都要注册
app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_account,url_prefix='/account')