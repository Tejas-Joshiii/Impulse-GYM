import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
os.makedirs("db", exist_ok=True)  # ensure folder exists

db_url = os.getenv("db_connection")
engine = create_engine(db_url, echo=True)