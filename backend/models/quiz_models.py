from extensions import db
from datetime import datetime

class Subject(db.Model):
    # LINE 5 (NEW): Explicitly define the table name as 'subjects' (plural).
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    chapters = db.relationship('Chapter', backref='subject', lazy=True, cascade="all, delete-orphan")

class Chapter(db.Model):
    # LINE 12 (NEW): Explicitly define the table name as 'chapters' (plural).
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # LINE 15 (CORRECTION): The foreign key must point to 'subjects.id'.
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    quizzes = db.relationship('Quiz', backref='chapter', lazy=True, cascade="all, delete-orphan")

class Quiz(db.Model):
    # LINE 20 (NEW): Explicitly define the table name as 'quizzes' (plural).
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    time_duration = db.Column(db.String(10)) # e.g., "00:30"
    # LINE 25 (CORRECTION): The foreign key must point to 'chapters.id'.
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    questions = db.relationship('Question', backref='quiz', lazy=True, cascade="all, delete-orphan")
    scores = db.relationship('Score', backref='quiz', lazy=True, cascade="all, delete-orphan")

class Question(db.Model):
    # LINE 31 (NEW): Explicitly define the table name as 'questions' (plural).
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.Text, nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    option4 = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.Integer, nullable=False)
    # LINE 40 (CORRECTION): The foreign key must point to 'quizzes.id'.
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)

class Score(db.Model):
    # LINE 44 (NEW): Explicitly define the table name as 'scores' (plural).
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    total_scored = db.Column(db.Integer, nullable=False)
    attempt_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    time_spent = db.Column(db.Integer, default=0)  # Time spent in seconds
    # LINE 50 (CORRECTION): The foreign key must point to 'users.id'.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # LINE 52 (CORRECTION): The foreign key must point to 'quizzes.id'.
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
