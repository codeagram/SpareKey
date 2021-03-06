from application import db
from datetime import datetime


class SpareKeyDB(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(32), nullable=False)
    loan_no = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32))
    added = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    recepient = db.Column(db.String(32))
    return_date = db.Column(db.Date)
    Expected_date = db.Column(db.Date)
    remarks = db.Column(db.String(100))


class FieldOfficers(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    is_active = db.Column(db.Boolean, default=True)
