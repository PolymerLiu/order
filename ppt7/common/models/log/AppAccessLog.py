# coding: utf-8
from application import db


class AppAccessLog(db.Model):
    __tablename__ = 'app_access_log'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='uid')
    referer_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='?????refer')
    target_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='???url')
    query_params = db.Column(db.Text, nullable=False, info='get?post??')
    ua = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='??ua')
    ip = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='??ip')
    note = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='json??????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
