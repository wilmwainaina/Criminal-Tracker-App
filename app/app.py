from flask import Flask, jsonify, request, abort
from flask_jwt_extended import jwt_required, JWTManager, create_access_token
from models import db, Crime, Criminal, Victim  # Replaced 'Suspect' with 'Criminal'
from flask_migrate import Migrate

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '111222333444555666'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///criminal_db"

jwt = JWTManager(app)
migrate = Migrate(app, db)

# Initialize the SQLAlchemy extension
db.init_app(app)

users = {
    'adam':{
        'username': "adam",
        'password':'kelly123',
        'role': ['user']
    }
}

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        username = request.json['username']
        password = request.json['password']


    if username in users and users['adam']['password'] == password:
      access_token = create_access_token(identity=username)
      return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid username or password'), 401

@app.route('/crimes', methods=['GET'])
@jwt_required
def get_crimes():
    crimes = Crime.query.all()
    return jsonify([crime.serialize for crime in crimes])

# Criminal routes
@app.route('/criminals', methods=['GET'])  # Replaced '/suspects' with '/criminals'
def get_criminals():  # Replaced 'get_suspects' with 'get_criminals'
    criminals = Criminal.query.all()  # Replaced 'Suspect' with 'Criminal'
    return jsonify([criminal.serialize for criminal in criminals])  # Replaced 'suspect' with 'criminal'

@app.route('/criminals', methods=['POST'])  # Replaced '/suspects' with '/criminals'
def post_criminal():  # Replaced 'post_suspect' with 'post_criminal'
    if not request.json or 'name' not in request.json:
        abort(400)
    criminal = Criminal(name=request.json['name'])  # Replaced 'Suspect' with 'Criminal'
    db.session.add(criminal)
    db.session.commit()
    return jsonify(criminal.serialize), 201  # Replaced 'suspect' with 'criminal'

@app.route('/criminals/<int:id>', methods=['GET', 'PUT', 'DELETE'])  # Replaced '/suspects' with '/criminals'
def handle_criminal(id):  # Replaced 'handle_suspect' with 'handle_criminal'
    criminal = Criminal.query.get(id)  # Replaced 'Suspect' with 'Criminal'
    if request.method == 'GET':
        return jsonify(criminal.serialize)  # Replaced 'suspect' with 'criminal'
    elif request.method == 'PUT':
        if 'name' in request.json:
            criminal.name = request.json['name']  # Replaced 'suspect' with 'criminal'
        db.session.commit()
        return jsonify(criminal.serialize)  # Replaced 'suspect' with 'criminal'
    elif request.method == 'DELETE':
        db.session.delete(criminal)  # Replaced 'suspect' with 'criminal'
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
    app.run(port=5000, debug=True)

