from flask import Blueprint, request, jsonify
from models import User, db, bcrypt
from flask_jwt_extended import create_access_token

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity={'username': user.username, 'email': user.email})
        return jsonify({'token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
