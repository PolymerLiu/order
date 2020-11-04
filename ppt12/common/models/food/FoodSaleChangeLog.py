from application import db

class FoodSaleChangeLog(db.Model):
    __tablename__ = 'food_sale_change_log'

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='??id')
    quantity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='????')
    price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='????')
    member_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='??id')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
