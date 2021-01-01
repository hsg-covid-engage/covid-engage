import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import json
#from flask_session import Session
#from flask.ext.session import Session

db = SQLAlchemy()

def create_app():
    """Construct the core application"""
    app = Flask(__name__)

    SESSION_TYPE = 'sqlalchemy'

    app.secret_key = 'thisgfrhfghhhhhhhhhhhhhhhhhhggggggggggggggfffffff'

    #session = Session()
    #app.config.from_object(__name__)
    #session.init_app(app)


    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db = SQLAlchemy(app)
    db.init_app(app)
    

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app
