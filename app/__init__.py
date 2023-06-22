#This app demonstrates basic RESTful API 
#utorial: https://www.google.com/search?q=tutorial+restful+api&oq=tutorial+restful+api&aqs=chrome..69i57j0i22i30l9.8227j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:aed5445a,vid:qbLc5a9jdXo

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks_data.db'
db = SQLAlchemy(app)

# Import models to ensure they are registered with SQLAlchemy
from app import models

# Create the database tables
with app.app_context():
    db.create_all()

# Import routes
from app import routes