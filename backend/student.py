# backend/student.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from models.user import User
from models.quiz_models import Quiz, Question, Score
from extensions import db

student_bp = Blueprint('student_bp', __name__)

# A decorator to check if the user is a student
def student_required():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            current_user_identity = get_jwt_identity()
            if current_user_identity.get('role') != 'student':
                return jsonify(message="Students only! Access denied."), 403
            # Find the user based on email from token
            user = User.query.filter_by(email=current_user_identity.get('email')).first()
            return fn(user, *args, **kwargs)
        return decorator
    return wrapper

@student_bp.route('/dashboard', methods=['GET'])
@student_required()
def dashboard_data(current_student):
    """
    Returns summary data for the student dashboard.
    """
    try:
        # Total quizzes available
        quizzes_available = Quiz.query.count()
        # Total quizzes attempted by this student
        quizzes_attempted = Score.query.filter_by(user_id=current_student.id).count()
        # Average marks for this student
        from sqlalchemy import func
        avg_marks_result = db.session.query(func.avg(Score.total_scored)).filter(Score.user_id == current_student.id).scalar()
        avg_marks = round(float(avg_marks_result), 2) if avg_marks_result is not None else 0
        # Total time spent: Score has no time_spent field, so set to 0 or calculate differently if needed
        time_spent = 0

        # Recent events: 3 most recent quizzes
        recent_quizzes = Quiz.query.order_by(Quiz.id.desc()).limit(3).all()
        recent_events = [
            {
                "title": quiz.title,
                "questions": quiz.questions.count() if hasattr(quiz, 'questions') else 0,
                "completions": Score.query.filter_by(quiz_id=quiz.id).count(),
                "completionRate": 0  # Placeholder, can be calculated if needed
            } for quiz in recent_quizzes
        ]

        dashboard_summary = {
            "summaryCards": [
                {"title": "Quizzes available", "value": quizzes_available},
                {"title": "Quizzes attempted", "value": quizzes_attempted},
                {"title": "Time spent", "value": time_spent},
                {"title": "Average marks", "value": avg_marks}
            ],
            "recentEvents": recent_events
        }
        return jsonify(dashboard_summary), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

@student_bp.route('/profile', methods=['GET'])
@student_required()
def student_profile(current_student):
    """
    Returns the student's profile information.
    """
    try:
        profile = {
            "full_name": current_student.full_name,
            "username": current_student.username,
            "email": current_student.email,
            "role": current_student.role
        }
        return jsonify(profile=profile), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

@student_bp.route('/quizzes', methods=['GET'])
@student_required()
def get_quizzes(current_student):
    """
    Returns a list of all available quizzes.
    """
    try:
        quizzes = Quiz.query.all()
        quiz_list = [
            {
                "id": quiz.id,
                "title": quiz.title,
                "created_at": str(getattr(quiz, 'created_at', ''))
            } for quiz in quizzes
        ]
        return jsonify(quizzes=quiz_list), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

@student_bp.route('/results', methods=['GET'])
@student_required()
def get_results(current_student):
    """
    Returns the student's quiz results.
    """
    try:
        results = Score.query.filter_by(user_id=current_student.id).all()
        result_list = [
            {
                "quiz_id": result.quiz_id,
                "total_scored": result.total_scored,
                "total_questions": result.total_questions,
                "completed_at": str(getattr(result, 'completed_at', ''))
            } for result in results
        ]
        return jsonify(results=result_list), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500
    
@student_bp.route('/about-quiz/<int:quiz_id>', methods=['GET'])
@student_required()
def about_quiz(current_student, quiz_id):
    """
    Returns detailed info for a quiz: subject, chapters, questions, difficulty, etc.
    """
    try:
        quiz = Quiz.query.get(quiz_id)
        if not quiz:
            return jsonify(message="Quiz not found"), 404

        # Get chapter and subject
        chapter = quiz.chapter
        subject = chapter.subject if chapter else None

        # Get all chapters for this subject
        chapters = []
        if subject:
            for ch in subject.chapters:
                chapters.append({
                    "id": ch.id,
                    "name": ch.name,
                    "questions": Question.query.filter_by(quiz_id=quiz.id,).count() if ch.id == chapter.id else 0
                })

        # Difficulty (placeholder, you can add a field to Quiz if needed)
        difficulty = getattr(quiz, 'difficulty', 'Medium')

        # Total questions in this quiz
        total_questions = Question.query.filter_by(quiz_id=quiz.id).count()

        data = {
            "quiz_id": quiz.id,
            "quiz_name": quiz.title,
            "subject": subject.name if subject else None,
            "chapter": chapter.name if chapter else None,
            "total_questions": total_questions,
            "difficulty": difficulty,
            "chapters": chapters
        }
        return jsonify(data), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500