# coding: utf-8
from application import db,app


class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???')
    mobile = db.Column(db.String(11), nullable=False, server_default=db.FetchedValue(), info='??????')
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 1?? 2??')
    avatar = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='????')
    salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='??salt')
    reg_ip = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??ip')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 1??? 0???')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')


    @property
    def status_desc(self):
        return app.config['STATUS_MAPPING'][str(self.status)]

    @property
    def sex_desc(self):
        sex_mapping = {
            '0':'未知',
            '1':'男',
            '2':'女',
        }
        return sex_mapping[str(self.status)]