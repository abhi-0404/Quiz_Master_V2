from flask_sqlalchemy import SQLAlchemy

# By defining the db object here, we can safely import it into any other
# file in our project without causing circular dependency errors.
db = SQLAlchemy()

