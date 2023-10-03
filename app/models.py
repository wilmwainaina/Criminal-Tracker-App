from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# Associative table for many to many relationship





class Crime(db.Model):
    __tablename__ = 'crime'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    victims = db.relationship('Victim', back_populates='crimes') # tis is a one to many relationship
    suspects = db.relationship('Suspect',
                            back_populates='crimes')


class Suspect(db.Model):
    __tablename__ ='suspect'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    crimes = db.relationship('Crime',
                          back_populates='suspects')




class Victim(db.Model):
    __tablename__ = 'victim'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    crimes_id = db.Column(db.Integer, db.ForeignKey('crime.id'))
    crimes = db.relationship('Crime', back_populates='victims') # this is a one to many relationship