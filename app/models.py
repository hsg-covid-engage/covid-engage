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
    date = db.Column(db.String(80))
    
    def to_json(self):
        return {
            #"id":int(self.id),
            #"id_user":int(self.id_user),
            #"fever":int(self.fever),
            #"cough":int(self.cough),
            #"myalgia":int(self.myalgia),
            #"sputum":int(self.sputum),
            #"hemoptysis":int(self.hemoptysis),
            #"diarrhea":int(self.diarrhea),
            #"smell_imparement":int(self.smell_imparement),
            #"taste_imparement":int(self.taste_imparement)
            "id":self.id,
            "id_user":self.id_user,
            "fever":self.fever,
            "cough":self.cough,
            "myalgia":self.myalgia,
            "sputum":self.sputum,
            "hemoptysis":self.hemoptysis,
            "diarrhea":self.diarrhea,
            "smell_imparement":self.smell_imparement,
            "taste_imparement":self.taste_imparement,
            "date":self.date


        }
    
   
    

