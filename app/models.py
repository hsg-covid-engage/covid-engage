"""Data Models"""
from . import db

class User(db.Model):
    __tablename__ = "user3"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '[%r]' % (self.name)
        #return '[%r, %r]' % (self.email, self.password)
        #return '<Users %r>' % self.name
        #return self.email
