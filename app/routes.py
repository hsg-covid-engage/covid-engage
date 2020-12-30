"""App Routes"""
from flask import Flask, render_template, request, redirect, session, jsonify
from flask import current_app as app
from .models import db, User, Symptoms
import json
import logging
from datetime import datetime
#from react import React, PureComponent
#from recharts import LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend 

logging.basicConfig(level=logging.DEBUG)


@app.route("/home_test")
def home_test():
    
    return render_template("home_test.html")

@app.route("/FAQ")
def FAQ():
    
    return render_template("FAQ.html")

@app.route("/")
def login():
    return render_template("login.html")
    #return "Hello World!"

@app.route("/register")
def register():
    return render_template("register.html")
    #return "Hello World!"

@app.route("/home")
def home():
    #if 'user_id' in session:
    return render_template("home.html",summary = json.dumps({"fever":[],"myalgia":[],
    "cough":[],"sputum":[],"hemoptysis":[],"diarrhea":[],"smell":[],"taste":[]}))
    #else:
    #    return redirect('/')

@app.route("/login_validation", methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    if str(User.query.filter_by(email=email).filter_by(password=password).first()) != 'None':
        return redirect('/home')
    else:
        return redirect('/')

    #cursor.execute("""SELECT * FROM 'users' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}'""".format(email,password))
    #users=cursor.fetchall()
    #if len(users)>0:
    # session['user_id']=users[0][0]
    #    return render_template('home.html') #redirect('/home.html')
    #else:
    #   return render_template('login.html') #redirect('/')

    #return "The email is {} and the password is {}".format(email,password)


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    db_user = User(name=name, email=email, password=password)
    db.session.add(db_user)
    db.session.commit()

    #cursor.execute("""INSERT INTO 'users' ('user_id', 'name', 'email', 'password') VALUES
    # (NULL, '{}','{}','{}')""".format(name,email,password))
    #conn.commit()

    #cursor.execute("""SELECT * FROM 'users' WHERE 'email' LIKE '{}'""".format(email))
    #myuser=cursor.fetchall()

    #session['user_id']=myuser[0][0]
    return redirect('/')
    #return "User registered successfully"


@app.route('/logout')
def logout():
    #session.pop('user_id')
    return redirect('/')
@app.route('/add_symptoms', methods=['POST'])
def add_symptoms():
    #https://python-forum.io/Thread-how-i-save-the-html-form-to-flask-database
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


    

    db_symptoms = Symptoms(fever=fever, cough=cough, myalgia=myalgia,sputum=sputum,hemoptysis=
    hemoptysis, diarrhea=diarrhea,smell_imparement=smell_imparement,taste_imparement=taste_imparement,date=date)
    db.session.add(db_symptoms)
    db.session.commit()
    return redirect('/home')

    #result = db.session.execute("SELECT * FROM symptoms WHERE id = : id", {"id":999} )

    # If no rows were returned (e.g., an UPDATE or DELETE), return an empty list
    #if result.returns_rows == False:
    #    response = []

    # Convert the response to a plain list of dicts
    #else:
    #    response = [dict(row.items()) for row in result]

    # Output the query result as JSON
    #print(json.dumps(response))


@app.route('/track', methods=['GET'])
def track():
    #summary = jsonify(json_list = Symptoms.query.all())
    ###summary = Symptoms.query.all()
    ###rec = json.dumps(summary)
    #result = summary.to_json
    ###records = [z.to_json() for z in Symptoms.query.first()]
    #print(summary)
    #return render_template('home_test.html', summary=summary)
    #!!!!!!!records = Symptoms.query.all().to_json()
    rec = Symptoms.query.all()
    
    #for i in range(len(rec)):
     #   x = rec[i].to_json()
    #xa = rec[0].to_json()
    #xb = rec[1].to_json()
    #a=json.dumps(xa)
    #b=json.dumps(xb)
    #b=json.dumps(xb)
    #ls=[]
    #ls.append(a)
    #ls.append(b)
    #d = dict(ls)
    #d=json.dump(rec,open("out.json","a+"))
    

    #result = []
    #for i in range(len(rec)):
    #    with open(i, "rb") as infile:
    #        result.append(json.load(infile))
    #x = json.loads(result)

    #with open("merged_file.json", "wb") as outfile:
    #    x=json.dump(result, outfile)


    #app.logger.info(rec)

    #records = summary.to_json
    #records = [z.to_json() for z in rec]
    #return render_template('home_test.html')
    #return str(rec)
    #one = rec[0].to_json()
    #two = rec[1].to_json()
    #three = one
    one = rec[0].to_json()
    ds = []
    for i in range(len(rec)):
        ds.append(rec[i].to_json())
    
    d = {}
    for k in one.keys():
        d[k] = tuple(d[k] for d in ds)
    #c = json.dumps(d)
    
    return render_template('home.html',summary=json.dumps(d))


