"""Data Models"""
from . import db

class User(db.Model):
    """Class that constructs the user database"""

    __tablename__ = "user9"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    location = db.Column(db.String(120))
    gender = db.Column(db.String(80))
    age = db.Column(db.String(80))
    smoking = db.Column(db.String(80))
    weight = db.Column(db.String(80))
    height = db.Column(db.String(80))
    phealth = db.Column(db.String(80))
    asthma = db.Column(db.String(80))
    diabetes = db.Column(db.String(80))
    heart = db.Column(db.String(80))
    liver = db.Column(db.String(80))
    kidney = db.Column(db.String(80))
    dysfunction = db.Column(db.String(80))
    distress = db.Column(db.String(80))
    pneumonia = db.Column(db.String(80))

    def __repr__(self):
        return '[%r]' % (self.name)



class Symptoms(db.Model):
    """Class that constructs the symptoms database"""

    __tablename__="symptoms6"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship('User', foreign_keys='Symptoms.id_user')

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
    
   
    

