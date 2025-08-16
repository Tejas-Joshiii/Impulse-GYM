import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
os.makedirs("db", exist_ok=True)  # ensure folder exists

db_url = os.getenv("db_connection")
engine = create_engine(db_url, echo=True)

def show_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        for row in result.all():
            print(dict(row._mapping))