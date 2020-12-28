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
class Symptoms(db.Model):
    __tablename__="symptoms"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user3.id'))
    user3 = db.relationship("User", backref=db.backref("user3", uselist=False))
    # see link: https://stackoverflow.com/questions/41569206/flask-sqlalchemy-foreign-key-relationships
    fever = db.Column(db.String)
    cough = db.Column(db.String)
    myalgia = db.Column(db.String)
    sputum = db.Column(db.String)
    hemoptysis = db.Column(db.String)
    diarrhea = db.Column(db.String)
    smell_imparement = db.Column(db.String)
    taste_imparement = db.Column(db.String)
    def __repr__(self):
        return '[%r]' % (self.fever)
    
   
    

