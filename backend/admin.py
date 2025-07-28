# backend/admin.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.quiz_models import Quiz, Question

admin_bp = Blueprint('admin_bp', __name__)

# A decorator to check if the user is an admin
def admin_required():
    def wrapper(fn):
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
    This endpoint queries the database and returns summary data for the admin dashboard.
    """
    try:
        # ========================================================================
        # --- CORRECTION STARTS HERE (Lines 40-57) ---
        # ========================================================================
        # LINES 40-44 (CORRECTION): Instead of mock data, we now query the database for real counts.
        total_quizzes = Quiz.query.count()
        total_questions = Question.query.count()
        total_students = User.query.filter_by(role='student').count()
        # For "Active Events", we'll just use the quiz count for now as a placeholder.
        
        # LINES 46-55 (CORRECTION): We structure the response to match what the frontend expects.
        dashboard_summary = {
            "summaryCards": [
                {"title": "Total Quizzes", "value": total_quizzes},
                {"title": "Active Events", "value": total_quizzes}, # Placeholder
                {"title": "Students", "value": total_students},
                {"title": "Total Questions", "value": total_questions}
            ],
            # These are placeholders for now, as we will build these features next.
            "recentEvents": [], 
            "recentQuizzes": []
        }
        
        return jsonify(dashboard_summary), 200
        # ========================================================================
        # --- CORRECTION ENDS HERE ---
        # ========================================================================
    except Exception as e:
        # Added error handling for database issues.
        return jsonify(message=f"An error occurred: {str(e)}"), 500
