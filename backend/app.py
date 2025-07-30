# backend/app.py
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

# Import extensions and models
from extensions import db
from models.user import User
from models.quiz_models import Subject, Chapter, Quiz, Question, Score 

# Import blueprints (routes)
from routes.auth import auth_bp
from admin import admin_bp 
from student import student_bp 

def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__)

    # --- Configuration ---
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizzy.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-super-secret-key-change-this'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

    # --- Initialize Extensions ---
    db.init_app(app)
    jwt = JWTManager(app)
    CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    # --- Register Blueprints ---
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(student_bp, url_prefix='/api/student')

    # --- Create Database and Admin User ---
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(email="admin@g.com").first():
            admin = User(
                full_name="Admin User",
                username="admin",
                email="admin@g.com",
                role="admin"
            )
            admin.set_password("123")
            db.session.add(admin)
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
