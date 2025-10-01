# app/db_check.py
from my_project import create_app
from my_project.database import db
from sqlalchemy import text

app = create_app()

with app.app_context():
    dbname = db.session.execute(text("SELECT DB_NAME()")).scalar()
    print("Connected to DB:", dbname)


