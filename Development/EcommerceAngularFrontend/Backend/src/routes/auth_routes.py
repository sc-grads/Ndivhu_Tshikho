from flask import Blueprint, request, jsonify
from model.user_model import User
from src import db, bcrypt, jwt
from flask_jwt_extended import create_access_token
import logging

auth_bp = Blueprint('auth', __name__)
logger = logging.getLogger(__name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    logger.info(f'Registration attempt for username: {username}, email: {email}')
    
    if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
        logger.warning(f'User already exists with username: {username} or email: {email}')
        return jsonify({"message": "User already exists"}), 400
    
    new_user = User(username=username, email=email, password=bcrypt.generate_password_hash(password).decode('utf-8'))
    db.session.add(new_user)
    try:
        db.session.commit()
        logger.info(f'User created successfully with username: {username}')
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f'Error creating user with username: {username}. Error: {e}')
        return jsonify({"message": "Internal Server Error"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    logger.info(f'Login attempt for email: {email}')
    
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        logger.info(f'Login successful for email: {email}')
        return jsonify(access_token=access_token), 200
    
    logger.warning(f'Invalid login attempt for email: {email}')
    return jsonify({"message": "Invalid credentials"}), 401
