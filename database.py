import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
os.makedirs("db", exist_ok=True)  # ensure folder exists

db_url = os.getenv("db_connection")
engine = create_engine(db_url, echo=True)

def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS exercise (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                quote TEXT,
                detail TEXT
            )
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS membership (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mem_id INT,
                fullName TEXT NOT NULL,
                emailId TEXT NOT NULL,
                phoneNo TEXT,
                address TEXT,
                membershipType TEXT
            )
        """))


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
        if len(rows) == 0: # agar list empty ho toh
            return None
        else:
            return rows[0]._asdict() # is list ka pehla tuple return kar raha hai us id no ki information

def add_membershipTodb(mem_id, data):
    with engine.begin() as conn:
        query = text("""INSERT INTO membership (mem_id, fullName, emailId, phoneNo, address, membershipType) VALUES (:mem_id, :fullName, :emailId, :phoneNo, :address, :membershipType)""")
        conn.execute(query,
                    {
                        'mem_id' : mem_id,
                        'fullName' : data['fullName'],
                        'emailId'  : data['emailId'],
                        'phoneNo'  : data['phoneNo'],
                        'address'  : data['address'],
                        'membershipType' : data['membershipType']
                }) # conn.execute ham pakra deta hai in variable me data through data['fullName'] then insert into wale m values m data hota hai na ki koi class ya css se relation hai

print("Using DB file at:", os.path.abspath("db/mydb.db"))