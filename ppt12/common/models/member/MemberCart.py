# coding: utf-8
from application import db


class MemberCart(db.Model):
    __tablename__ = 'member_cart'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='??id')
    food_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='??id')
    quantity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='??')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
