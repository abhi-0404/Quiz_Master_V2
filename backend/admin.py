# backend/admin.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from models.user import User
from models.quiz_models import Quiz, Question, Subject, Chapter, Score
from extensions import db


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

@admin_bp.route('/events/<int:quiz_id>', methods=['PUT'])
@admin_required()
def edit_quiz(current_admin, quiz_id):
    from flask import request
    data = request.get_json()
    try:
        quiz = Quiz.query.get_or_404(quiz_id)
        quiz.title = data.get('title', quiz.title)
        quiz.description = data.get('description', getattr(quiz, 'description', ''))
        quiz.category = data.get('category', getattr(quiz, 'category', ''))
        quiz.difficulty = data.get('difficulty', getattr(quiz, 'difficulty', ''))
        quiz.date_time = data.get('date_time', getattr(quiz, 'date_time', None))
        quiz.time_duration = data.get('time_duration', getattr(quiz, 'time_duration', None))
        db.session.commit()
        return jsonify(message="Quiz updated"), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# --- API: Get subjects for a quiz ---
@admin_bp.route('/quiz/<int:quiz_id>/subjects', methods=['GET'])
@admin_required()
def get_subjects_for_quiz(current_admin, quiz_id):
    try:
        # Find the chapter for this quiz
        quiz = Quiz.query.get_or_404(quiz_id)
        chapter = quiz.chapter
        if not chapter:
            return jsonify(subjects=[]), 200
        subject = chapter.subject
        if not subject:
            return jsonify(subjects=[]), 200
        # Return as a list for frontend consistency
        return jsonify(subjects=[{
            "id": subject.id,
            "title": subject.name,
            "description": subject.description
        }]), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# --- API: Get chapters for a subject ---
@admin_bp.route('/subject/<int:subject_id>/chapters', methods=['GET'])
@admin_required()
def get_chapters_for_subject(current_admin, subject_id):
    try:
        chapters = Chapter.query.filter_by(subject_id=subject_id).all()
        chapter_list = [{
            "id": c.id,
            "title": c.name,
            "questions": len(c.quizzes)
        } for c in chapters]
        return jsonify(chapters=chapter_list), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# --- API: Get questions for a chapter ---
@admin_bp.route('/chapter/<int:chapter_id>/questions', methods=['GET'])
@admin_required()
def get_questions_for_chapter(current_admin, chapter_id):
    try:
        quizzes = Quiz.query.filter_by(chapter_id=chapter_id).all()
        questions = []
        for quiz in quizzes:
            for q in quiz.questions:
                # Only return non-empty options
                options = [opt for opt in [q.option1, q.option2, q.option3, q.option4] if opt]
                questions.append({
                    "id": q.id,
                    "statement": q.statement,
                    "options": options,
                    "correct_option": q.correct_option
                })
        return jsonify(questions=questions), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# --- CRUD endpoints for Quiz, Subject, Chapter, Question ---
# Create Subject
@admin_bp.route('/subject', methods=['POST'])
@admin_required()
def create_subject(current_admin):
    from flask import request
    data = request.get_json()
    try:
        subject = Subject(name=data['name'], description=data.get('description'))
        db.session.add(subject)
        db.session.commit()
        return jsonify(message="Subject created", id=subject.id), 201
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# Edit Subject
@admin_bp.route('/subject/<int:subject_id>', methods=['PUT'])
@admin_required()
def edit_subject(current_admin, subject_id):
    from flask import request
    data = request.get_json()
    try:
        subject = Subject.query.get_or_404(subject_id)
        subject.name = data.get('name', subject.name)
        subject.description = data.get('description', subject.description)
        db.session.commit()
        return jsonify(message="Subject updated"), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# Delete Subject
@admin_bp.route('/subject/<int:subject_id>', methods=['DELETE'])
@admin_required()
def delete_subject(current_admin, subject_id):
    try:
        subject = Subject.query.get_or_404(subject_id)
        db.session.delete(subject)
        db.session.commit()
        return jsonify(message="Subject deleted"), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500


# Create Chapter
@admin_bp.route('/chapter', methods=['POST'])
@admin_required()
def create_chapter(current_admin):
    from flask import request
    data = request.get_json()
    try:
        chapter = Chapter(
            name=data['name'],
            subject_id=data['subject_id'],
            description=data.get('description')
        )
        db.session.add(chapter)
        db.session.commit()
        return jsonify(message="Chapter created", id=chapter.id), 201
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# Edit Chapter
@admin_bp.route('/chapter/<int:chapter_id>', methods=['PUT'])
@admin_required()
def edit_chapter(current_admin, chapter_id):
    from flask import request
    data = request.get_json()
    try:
        chapter = Chapter.query.get_or_404(chapter_id)
        chapter.name = data.get('name', chapter.name)
        chapter.description = data.get('description', chapter.description)
        db.session.commit()
        return jsonify(message="Chapter updated"), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# Delete Chapter
@admin_bp.route('/chapter/<int:chapter_id>', methods=['DELETE'])
@admin_required()
def delete_chapter(current_admin, chapter_id):
    try:
        chapter = Chapter.query.get_or_404(chapter_id)
        db.session.delete(chapter)
        db.session.commit()
        return jsonify(message="Chapter deleted"), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# Create Question
@admin_bp.route('/question', methods=['POST'])
@admin_required()
def create_question(current_admin):
    from flask import request
    data = request.get_json()
    try:
        # Accepts options as a list (minimum 2, maximum 4)
        options = data.get('options', [])
        if not isinstance(options, list) or not (2 <= len(options) <= 4):
            return jsonify(message="Options must be a list of 2 to 4 items."), 400
        # Pad options to 4 for DB columns
        padded = options + [''] * (4 - len(options))
        question = Question(
            statement=data['statement'],
            option1=padded[0],
            option2=padded[1],
            option3=padded[2],
            option4=padded[3],
            correct_option=data['correct_option'],
            quiz_id=data['quiz_id'],
            points=data.get('points', 0)
        )
        db.session.add(question)
        db.session.commit()
        return jsonify(message="Question created", id=question.id), 201
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# Edit Question
@admin_bp.route('/question/<int:question_id>', methods=['PUT'])
@admin_required()
def edit_question(current_admin, question_id):
    from flask import request
    data = request.get_json()
    try:
        question = Question.query.get_or_404(question_id)
        question.statement = data.get('statement', question.statement)
        options = data.get('options')
        if options:
            if not isinstance(options, list) or not (2 <= len(options) <= 4):
                return jsonify(message="Options must be a list of 2 to 4 items."), 400
            padded = options + [''] * (4 - len(options))
            question.option1 = padded[0]
            question.option2 = padded[1]
            question.option3 = padded[2]
            question.option4 = padded[3]
        else:
            question.option1 = data.get('option1', question.option1)
            question.option2 = data.get('option2', question.option2)
            question.option3 = data.get('option3', question.option3)
            question.option4 = data.get('option4', question.option4)
        question.correct_option = data.get('correct_option', question.correct_option)
        question.points = data.get('points', question.points)
        db.session.commit()
        return jsonify(message="Question updated"), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

# Delete Question
@admin_bp.route('/question/<int:question_id>', methods=['DELETE'])
@admin_required()
def delete_question(current_admin, question_id):
    try:
        question = Question.query.get_or_404(question_id)
        db.session.delete(question)
        db.session.commit()
        return jsonify(message="Question deleted"), 200
    except Exception as e:
        return jsonify(message=f"An error occurred: {str(e)}"), 500

@admin_bp.route('/dashboard', methods=['GET'])
@admin_required()
def dashboard_data(current_admin):
    """
    returns summary data for the admin dashboard.
    """
    try:
        # Fetch summary data
        total_quizzes = Quiz.query.count()
        total_quiz_attempts = Score.query.count()
        avg_marks = 0
        total_students = User.query.filter_by(role='student').count()

        # Calculate average marks if there are attempts
        from sqlalchemy import func
        avg_marks_result = db.session.query(func.avg(Score.total_scored)).scalar()
        if avg_marks_result is not None:
            avg_marks = round(float(avg_marks_result), 2)

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
                {"title": "Quizzes", "value": total_quizzes},
                {"title": "Quiz Attempts", "value": total_quiz_attempts},
                {"title": "AverageMarks", "value": avg_marks},
                {"title": "Students", "value": total_students}
            ],
            "recentEvents": recent_quizzes_list
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
                "description": getattr(event, 'description', ''),
                "category": getattr(event, 'category', ''),
                "difficulty": getattr(event, 'difficulty', ''),
                "date_time": str(getattr(event, 'date_time', '')),
                "time_duration": getattr(event, 'time_duration', None),
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
            description=data.get('description', ''),
            category=data.get('category', ''),
            difficulty=data.get('difficulty', ''),
            date_time=data.get('date_time'),
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
