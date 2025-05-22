# Estrutura do banco de dados, como criação de tabelas, conexôes etc.
# local: back/database/init_db.py

# from app import db
# from models import Usuario, Jogo, Historico
# from app import create_app

# app = create_app()

# with app.app_context():
#     db.create_all()
#     print("Banco de dados criado com sucesso!")

import sqlite3
from config import Config

def get_connection():
    return sqlite3.connect(Config.DATABASE_NAME)
