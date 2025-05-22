# Configurações globais
# Local: back/config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sua_chave_secreta')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'sua_jwt_secreta')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'quizDB.db')

