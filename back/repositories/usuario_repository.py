import sqlite3

def cadastrar_usuario_db(nickname, senha):
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO usuarios (nickname, senha)
        VALUES (?, ?)
    ''', (nickname, senha))
    conn.commit()
    conn.close()




# # Tudo que acessa o bonco (o que está no "banco/")

# from app import db
# from werkzeug.security import generate_password_hash, check_password_hash

# class Usuario(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     senha_hash = db.Column(db.String(128), nullable=False)

# class UsuarioRepository:
#     def criar_usuario(self, dados):
#         senha_hash = generate_password_hash(dados['senha'])
#         novo_usuario = Usuario(email=dados['email'], senha_hash=senha_hash)
#         db.session.add(novo_usuario)
#         db.session.commit()
#         return novo_usuario

#     def autenticar_usuario(self, email, senha):
#         usuario = Usuario.query.filter_by(email=email).first()
#         if usuario and check_password_hash(usuario.senha_hash, senha):
#             return usuario
#         return None


# import sqlite3

# def cadastrar_usuario_db(nickname, senha):
#     conn = sqlite3.connect("usuarios.db")
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO usuarios (nickname, senha)
#         VALUES (?, ?)
#     ''', (nickname, senha))
#     conn.commit()
#     conn.close()
