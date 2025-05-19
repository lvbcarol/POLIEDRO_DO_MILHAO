from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Criação do banco (apenas uma vez)
def criar_tabela():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

# Rota de cadastro
@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()

    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    if not nome or not email or not senha:
        return jsonify({'mensagem': 'Dados incompletos'}), 400

    try:
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha)
            VALUES (?, ?, ?)
        ''', (nome, email, senha))
        conn.commit()
        conn.close()

        return jsonify({'mensagem': 'Usuário cadastrado com sucesso'}), 201

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
