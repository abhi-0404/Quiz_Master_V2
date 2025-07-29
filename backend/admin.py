# backend/admin.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from models.user import User
from models.quiz_models import Quiz, Question

admin_bp = Blueprint('admin_bp', __name__)

# A decorator to check if the user is an admin
def admin_required():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            current_user_identity = get_jwt_identity()
            if current_user_identity.get('role') != 'admin':
                return jsonify(message="Admins only! Access denied."), 403

            # Find the user based on email from token
            user = User.query.filter_by(email=current_user_identity.get('email')).first()
            return fn(user, *args, **kwargs)
        return decorator
    return wrapper

@admin_bp.route('/dashboard', methods=['GET'])
@admin_required()
def dashboard_data(current_admin):
    """
    returns summary data for the admin dashboard.
    """
    try:
        # Fetch summary data
        total_quizzes = Quiz.query.count()
        total_questions = Question.query.count()
        total_students = User.query.filter_by(role='student').count()
        
        # Fetch 5 most recent quizzes as events
        recent_quizzes = Quiz.query.order_by(Quiz.id.desc()).limit(5).all()
        recent_quizzes_list = [
            {
                "id": quiz.id,
                "title": getattr(quiz, 'title', None),
                "created_at": str(getattr(quiz, 'created_at', ''))
            } for quiz in recent_quizzes
        ]

        dashboard_summary = {
            "summaryCards": [
                {"title": "Total Quizzes", "value": total_quizzes},
                {"title": "Active Events", "value": total_quizzes},
                {"title": "Students", "value": total_students},
                {"title": "Total Questions", "value": total_questions}
            ],
            "recentEvents": recent_quizzes_list,
            "recentQuizzes": recent_quizzes_list
        }
        return jsonify(dashboard_summary), 200
    except Exception as e:
        # Added error handling for database issues.
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# --- New admin routes ---
@admin_bp.route('/events', methods=['GET'])
@admin_required()
def get_events(current_admin):
    """
    Returns a list of events.
    """
    try:
        events = Quiz.query.all()
        event_list = [
            {
                "id": event.id,
                "title": getattr(event, 'title', None),
                "created_at": str(getattr(event, 'created_at', ''))
            } for event in events
        ]
        return jsonify(events=event_list), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

@admin_bp.route('/create-quiz', methods=['POST'])
@admin_required()
def create_quiz(current_admin):
    """
    Creates a new quiz.
    """
    from flask import request
    data = request.get_json()
    try:
        # Accept all relevant fields for Quiz creation
        new_quiz = Quiz(
            title=data.get('title'),
            chapter_id=data.get('chapter_id'),
            time_duration=data.get('time_duration')
        )
        from extensions import db
        db.session.add(new_quiz)
        db.session.commit()
        return jsonify(message="Quiz created successfully", quiz_id=new_quiz.id), 201
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

@admin_bp.route('/profile', methods=['GET'])
@admin_required()
def admin_profile(current_admin):
    """
    Returns the admin's profile information.
    """
    try:
        profile = {
            "full_name": current_admin.full_name,
            "username": current_admin.username,
            "email": current_admin.email,
            "role": current_admin.role
        }
        return jsonify(profile=profile), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

@admin_bp.route('/students', methods=['GET'])
@admin_required()
def get_students(current_admin):
    """
    Returns a list of all students.
    """
    try:
        students = User.query.filter_by(role='student').all()
        student_list = [
            {
                "id": student.id,
                "full_name": student.full_name,
                "username": student.username,
                "email": student.email
            } for student in students
        ]
        return jsonify(students=student_list), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500
