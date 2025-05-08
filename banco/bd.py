import sqlite3

def setup_database():
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()

    # Tabela usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            ID_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT NOT NULL,
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
            FOREIGN KEY(ID_usuario) REFERENCES usuarios(ID_usuario)
        );
    ''')

    conn.commit()
    conn.close()

# Executar função
setup_database()
print("Banco de dados criado com sucesso!")

c:\Users\carol\OneDrive\códigos pessoais\palacio das pecas\PROJETO_MILHAO\quizDB.db