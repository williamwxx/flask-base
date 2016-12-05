# coding=utf-8
from . import db
class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    Text = db.Column(db.Text)
    T_done = db.Column(db.Boolean,default=True)