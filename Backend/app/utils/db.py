import sqlite3
from flask import g
from config import Config

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            Config.DATABASE_NAME,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db_command():
    """Clear existing data and create new tables."""
    conn = sqlite3.connect(Config.DATABASE_NAME)
    cursor = conn.cursor()

    # Tabela usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            ID_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        );
    ''')

    # Tabela questões com resposta correta
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questoes (
            ID_questao INTEGER PRIMARY KEY AUTOINCREMENT,
            enunciado TEXT NOT NULL,
            alternativaA TEXT NOT NULL,
            alternativaB TEXT NOT NULL,
            alternativaC TEXT NOT NULL,
            alternativaD TEXT NOT NULL,
            resposta_correta CHAR(1) NOT NULL,
            dica TEXT,
            valor INTEGER,
            nivel_dificuldade TEXT
        );
    ''')

    # Tabela tentativas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tentativas (
            ID_tentativa INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_usuario INTEGER,
            valor_total INTEGER,
            data_tentativa TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(ID_usuario) REFERENCES usuarios(ID_usuario)
        );
    ''')

    conn.commit()
    conn.close()
    print("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(close_db)
    # app.cli.add_command(init_db_command) # We'll call init_db_command manually for now or via run.py

