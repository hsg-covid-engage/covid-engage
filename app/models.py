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
    #user_id = Column(Integer, ForeignKey('user3.id'))
    #user3 = relationship("User", backref=backref(user3, uselist=False))
    # see link: https://stackoverflow.com/questions/41569206/flask-sqlalchemy-foreign-key-relationships
    fever = db.Column(db.Integer)
    cough = db.Column(db.Integer)
    myalgia = db.Column(db.Integer)
    sputum = db.Column(db.Integer)
    hemoptysis = db.Column(db.Integer)
    diarrhea = db.Column(db.Integer)
    smell_imparement = db.Column(db.Integer)
    taste_imparement = db.Column(db.Integer)
    def __repr__(self):
        return '[%r]' % (self.name)
    

