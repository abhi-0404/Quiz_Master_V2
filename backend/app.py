from datetime import datetime
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource
from datetime import timedelta
from flask_cors import cross_origin

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type, Authorization'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["JWT_SECRET_KEY"] = "aStrongSecretKey"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
db = SQLAlchemy(app)
jwt = JWTManager(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default="employee")
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='assigned_user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default="pending")
    deadline = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    assigned_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

with app.app_context():
    db.create_all() 

class Hello(Resource):
    @cross_origin()
    @jwt_required()
    def get(self):
        user_name = get_jwt_identity()
        return jsonify({'msg': "hello world! from flask restful", 'user_name': user_name})

class SignupResource(Resource):
    @cross_origin()
    def post(self):
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'message': 'Username or Email already exists'})

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"username": username, "email": email}

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.username)
            response = jsonify({"msg":"successfully logged in", "token": access_token})
            return make_response(response, 401)
        response = jsonify({"msg": "email or password incorrect."})
        return make_response(response, 200)

api.add_resource(Hello, '/hello')
api.add_resource(SignupResource, '/signup')
api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="127.0.0.1")