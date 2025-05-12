import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    # JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", os.urandom(24))
    SECRET_KEY = "teste"
    JWT_SECRET_KEY = "teste"
    DATABASE_NAME = "quizDB.db"

