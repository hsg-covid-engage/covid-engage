"""App Routes"""
from flask import Flask, render_template, request, redirect, session, jsonify
from flask import current_app as app
from .models import db, User, Symptoms
import json
import logging
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)


@app.route("/home_test")
def home_test():
    """BITTE ERGAENZEN"""
    return render_template("home_test.html")

@app.route("/FAQ")
def FAQ():
    """Route to the FAQ page"""
    return render_template("FAQ.html")

@app.route("/")
def login():
    """Route to the login page"""
    return render_template("login.html")
   

@app.route("/register")
def register():
    """Route to the register page"""
    return render_template("register.html")


@app.route("/home")
def home():
    """BITTE ERGAENZEN"""
    return render_template("home.html",summary = json.dumps({"fever":[],"myalgia":[],
    "cough":[],"sputum":[],"hemoptysis":[],"diarrhea":[],"smell":[],"taste":[]}))


@app.route("/login_validation", methods=['POST'])
def login_validation():
    """Check login data"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).filter_by(password=password).first()
  
    if user: 
        session['user_id'] = int(user.id)
        return redirect('/home')
    else:
        return redirect('/')




@app.route('/add_user', methods=['POST'])
def add_user():
    """Register a new user and add data to the database"""

    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    gender = request.form.get('gender')
    age = request.form.get('age')
    smoking = request.form.get('smoking')
    weight = request.form.get('weight')
    height = request.form.get('height')
    phealth = request.form.get('phealth')
    asthma = request.form.get('asthma')
    diabetes = request.form.get('diabetes')
    heart = request.form.get('heart')
    liver = request.form.get('liver')
    kidney = request.form.get('kidney')
    dysfunction = request.form.get('dysfunction')
    distress = request.form.get('distress')
    pneumonia = request.form.get('pneumonia')

    db_user = User(name=name,  email=email, password=password, gender=gender, age=age, smoking=smoking, weight=weight, height=height, phealth=phealth,asthma=asthma, diabetes=diabetes, heart=heart, liver=liver, kidney=kidney, dysfunction=dysfunction, distress=distress, pneumonia=pneumonia)
    db.session.add(db_user)
    db.session.commit()

    return redirect('/')



@app.route('/logout')
def logout():
    """Logout the user and route to the start page"""
    return redirect('/')


@app.route('/add_symptoms', methods=['POST'])
def add_symptoms():
    """Add symptoms to the database"""
    
    user_id = session.get('user_id')
    
    fever = float(request.form.get('fever'))
    cough = int(request.form.get('cough'))
    myalgia = int(request.form.get('myalgia'))
    sputum = int(request.form.get('sputum'))
    hemoptysis= int(request.form.get('hemoptysis'))
    diarrhea = int(request.form.get('diarrhea'))
    smell_imparement = int(request.form.get('smell'))
    taste_imparement = int(request.form.get('taste'))

    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')
    date = formatted_date


    db_symptoms = Symptoms(id_user=user_id, fever=fever, cough=cough, myalgia=myalgia,sputum=sputum,hemoptysis=
    hemoptysis, diarrhea=diarrhea,smell_imparement=smell_imparement,taste_imparement=taste_imparement,date=date)
    db.session.add(db_symptoms)
    db.session.commit()

    return redirect('/home')




@app.route('/track', methods=['GET'])
def track():
    """Send historical symptoms data from database to charts"""

    rec = Symptoms.query.filter(Symptoms.id_user==session.get('user_id')).all()

    try:
        one = rec[0].to_json()
        ds = []
        for i in range(len(rec)):
            ds.append(rec[i].to_json())
        
        d = {}
        for k in one.keys():
            d[k] = tuple(d[k] for d in ds)
        
        
        return render_template('home.html',summary=json.dumps(d))
    
    except IndexError:
        return redirect('/home')


