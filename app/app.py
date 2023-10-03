from flask import Flask, jsonify, request, abort
from flask_jwt_extended import jwt_required, JWTManager, create_access_token
from models import db, Crime, Suspect, Victim
from flask_migrate import Migrate
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '111222333444555666'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///criminal_db"

jwt = JWTManager(app)
migrate = Migrate(app, db)
# Initialize the SQLAlchemy extension
db.init_app(app)

users = {
    'hamida':{
        'username': "hamida",
        'password':'mids123',
        'role': ['user']
    }
    }

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        username = request.json['username']
        password = request.json['password']


    if username in users and users['hamida']['password'] == password:
      access_token = create_access_token(identity=username)
      return jsonify(access_token=access_token), 200
    else:
      return jsonify(message='Invalid username or password'), 401

@app.route('/crimes', methods=['GET'])
@jwt_required
def get_crimes():
    crimes = Crime.query.all()
    return jsonify([crime.serialize for crime in crimes])

# @app.route('/crimes', methods=['POST'])
# @jwt_required
# def post_crime():
#     if not request.json or not 'name' in request.json:
#         abort(400)
#     crime = Crime(name=request.json['name'], description=request.json.get('description', ""))
#     db.session.add(crime)
#     db.session.commit()
#     return jsonify(crime.serialize), 201
  
# Suspect routes
@app.route('/suspects', methods=['GET'])
def get_suspects():
    suspects = Suspect.query.all()
    return jsonify([suspect.serialize for suspect in suspects])

@app.route('/suspects', methods=['POST'])
def post_suspect():
     if not request.json or 'name' not in request.json:
        abort(400)
     suspect = Suspect(name=request.json['name'])
     db.session.add(suspect)
     db.session.commit()
     return jsonify(suspect.serialize), 201

@app.route('/suspects/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_suspect(id):
    suspect = Suspect.query.get(id)
    if request.method == 'GET':
        return jsonify(suspect.serialize)
    elif request.method == 'PUT':
        if 'name' in request.json:
            suspect.name = request.json['name']
        db.session.commit()
        return jsonify(suspect.serialize)
    elif request.method == 'DELETE':
        db.session.delete(suspect)
        db.session.commit()
        return jsonify({"result": True})


# Victim routes
@app.route('/victims', methods=['GET'])
def get_victims():
    victims = Victim.query.all()
    return jsonify([victim.serialize for victim in victims])

@app.route('/victims', methods=['POST'])
def post_victim():
    if not request.json or 'name' not in request.json:
        abort(400)
    victim = Victim(name=request.json['name'])
    db.session.add(victim)
    db.session.commit()
    return jsonify(victim.serialize), 201

@app.route('/victims/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_victim(id):
    victim = Victim.query.get(id)
    if request.method == 'GET':
        return jsonify(victim.serialize)
    elif request.method == 'PUT':
        if 'name' in request.json:
            victim.name = request.json['name']
        db.session.commit()
        return jsonify(victim.serialize)
    elif request.method == 'DELETE':
        db.session.delete(victim)
        db.session.commit()
        return jsonify({"result": True})
    

if __name__ == '__main__':
    app.run(debug=True)

