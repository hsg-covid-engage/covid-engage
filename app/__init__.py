import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import json


db = SQLAlchemy()

def create_app():
    """Construct the core application"""
    app = Flask(__name__)

    SESSION_TYPE = 'sqlalchemy'

    app.secret_key = 'asflaksjflajfklaj'




    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    db.init_app(app)
    

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app
