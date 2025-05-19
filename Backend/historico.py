from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Cria o banco e a tabela se não existirem
def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            valor_ganho REAL,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco ao iniciar o servidor
init_db()

# Rota para salvar tentativa
@app.route('/salvar_tentativa', methods=['POST'])
def salvar_tentativa():
    data = request.get_json()
    nome = data.get('nome')
    valor = data.get('valor_ganho')
    data_tentativa = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO historico (nome, valor_ganho, data)
        VALUES (?, ?, ?)
    ''', (nome, valor, data_tentativa))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Tentativa salva com sucesso'})

# Rota para buscar histórico de um jogador
@app.route('/historico/<nome>', methods=['GET'])
def obter_historico(nome):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT valor_ganho, data
        FROM historico
        WHERE nome = ?
        ORDER BY id DESC
    ''', (nome,))
    tentativas = cursor.fetchall()
    conn.close()

    return jsonify([
        {'valor_ganho': valor, 'data': data}
        for valor, data in tentativas
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
