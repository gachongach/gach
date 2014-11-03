"""
models.py

"""
from apps import db

#
# add User Model
class User(db.Model):
    id = db.Column(db.String(64), primary_key = True)
    pw = db.Column(db.String(64))
    status = db.Column(db.Integer)
    score = db.Column(db.Integer)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.relationship('User', backref=db.backref('user_id_article', cascade='all, delete-orphan', lazy='dynamic'))
    author = db.Column(db.String(64), db.ForeignKey('user.id'))
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default = db.func.now())

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    article = db.relationship('Article', backref=db.backref('reply', cascade='all, delete-orphan', lazy='dynamic'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    date_created = db.Column(db.DateTime(), default = db.func.now())
    content = db.Column(db.String(255))
    user = db.relationship('User', backref=db.backref('user_id_reply', cascade='all, delete-orphan', lazy='dynamic'))
    author = db.Column(db.String(64), db.ForeignKey('user.id'))

