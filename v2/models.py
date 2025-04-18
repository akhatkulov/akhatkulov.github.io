from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    link = db.Column(db.String(200), nullable=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    about = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=True)
    feedback_link = db.Column(db.String(200), nullable=True)
