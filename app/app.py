from flask import Flask, jsonify, request, abort
from flask_jwt_extended import jwt_required, JWTManager, create_access_token
from models import db, Crime, Criminal,  Victim  # Replaced 'Criminal' with 'Criminal'
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    token = []
    if request.is_json:
        username = request.json['username']
        password = request.json['password']
    

        if username in users and users['adam']['password'] == password:
            access_token = create_access_token(identity=username)
            print(access_token)
            token.append(access_token)
            return jsonify(access_token=access_token), 200
        return jsonify(message='Invalid username or password'), 401
        
    # return jsonify(message='Invalid input'), 200
    return jsonify(token=token), 200


@app.route('/home', methods=['GET'])
def home():
    return jsonify(message='Welcome to Crime API'), 200



@app.route('/crimes', methods=['GET'])
@jwt_required()
def get_crimes():
    crimes = Crime.query.all()
    return jsonify([crime.serialize for crime in crimes])

# Criminal routes
@app.route('/criminals', methods=['GET'])  # Replaced '/Criminals' with '/criminals'
def get_criminals():  # Replaced 'get_Criminals' with 'get_criminals'
    criminals = Criminal.query.all()  # Replaced 'Criminal' with 'Criminal'
    return jsonify([criminal.serialize for criminal in criminals])  # Replaced 'Criminal' with 'criminal'

@app.route('/criminals', methods=['POST'])  # Replaced '/Criminals' with '/criminals'
def post_criminal():  # Replaced 'post_Criminal' with 'post_criminal'
    if not request.json or 'name' not in request.json:
        abort(400)
    criminal = Criminal(name=request.json['name'])  # Replaced 'Criminal' with 'Criminal'
    db.session.add(criminal)
    db.session.commit()
    return jsonify(criminal.serialize), 201  # Replaced 'Criminal' with 'criminal'

@app.route('/criminals/<int:id>', methods=['GET', 'PUT', 'DELETE'])  # Replaced '/Criminals' with '/criminals'
def handle_criminal(id):  # Replaced 'handle_Criminal' with 'handle_criminal'
    criminal = Criminal.query.get(id)  # Replaced 'Criminal' with 'Criminal'
    if request.method == 'GET':
        return jsonify(criminal.serialize)  # Replaced 'Criminal' with 'criminal'
    elif request.method == 'PUT':
        if 'name' in request.json:
            criminal.name = request.json['name']  # Replaced 'Criminal' with 'criminal'
        db.session.commit()
        return jsonify(criminal.serialize)  # Replaced 'Criminal' with 'criminal'
    elif request.method == 'DELETE':
        db.session.delete(criminal)  # Replaced 'Criminal' with 'criminal'
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

