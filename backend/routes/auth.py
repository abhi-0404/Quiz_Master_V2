from flask import request, jsonify, Blueprint
from extensions import db
from models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

# Correct blueprint name
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """Handles new user registration."""
    data = request.get_json()
    if not data or not all(k in data for k in ('full_name', 'username', 'email', 'password')):
        return jsonify({'message': 'Missing data for required fields'}), 400

    if User.query.filter((User.email == data['email']) | (User.username == data['username'])).first():
        return jsonify({'message': 'User with this email or username already exists'}), 409

    new_user = User(
        full_name=data['full_name'],
        username=data['username'],
        email=data['email'],
        role='student'  # default role
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    access_token = create_access_token(identity={"email": user.email, "role": user.role})

    return jsonify({
        'access_token': access_token,
        'role': user.role,
        'message': 'Login successfully!'
    }), 200
