from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


db = SQLAlchemy()


# Associative table for many to many relationship





class Crime(db.Model):
    __tablename__ = 'crimes'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    victims = db.relationship('Victim', back_populates='crimes') # tis is a one to many relationship
    criminals = db.relationship('Criminal',
                            back_populates='crimes')


class Criminal (db.Model):
    __tablename__ ='criminal'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    crimes = db.relationship('Crime',
                          back_populates='criminals')




class Victim(db.Model):
    __tablename__ = 'victim'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    crimes_id = db.Column(db.Integer, db.ForeignKey('crime.id'))
    crimes = db.relationship('Crime', back_populates='victims') # this is a one to many relationship