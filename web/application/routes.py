"""App Routes"""
from flask import Flask, render_template, request, redirect, session
from flask import current_app as app
from .models import db, User

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
    return render_template("home.html")
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