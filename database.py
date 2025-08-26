import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
os.makedirs("db", exist_ok=True)  # ensure folder exists

db_url = os.getenv("db_connection")
engine = create_engine(db_url, echo=True)

def init_db():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS exercise (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                quote TEXT,
                detail INT
            )
        """))
        conn.commit()

def load_workout_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM exercise"))
        exercise = []
        for row in result.all():
            exercise.append(row._asdict())
        return exercise

def load_workouts_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM exercise WHERE id = :val"), {"val": id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict() # is list ka pehla tuple return kar raha hai us id no ki information

            