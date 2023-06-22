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