from flask import Flask, request, jsonify
import sqlite3
import random

app = Flask(__name__)
conn = sqlite3.connect('quiz.db', check_same_thread=False)

# Embaralha e retorna uma pergunta diferente a cada vez
def obter_pergunta_aleatoria(perguntas_usadas):
    cursor = conn.cursor()
    query = "SELECT * FROM perguntas WHERE id NOT IN ({seq}) ORDER BY RANDOM() LIMIT 1".format(
        seq=','.join(['?'] * len(perguntas_usadas)) if perguntas_usadas else '0'
    )
    cursor.execute(query, perguntas_usadas if perguntas_usadas else [])
    row = cursor.fetchone()
    if not row:
        return None
    pergunta = {
        'id': row[0],
        'pergunta': row[1],
        'alternativas': [row[2], row[3], row[4], row[5]],
        'resposta_correta': row[6],
        'dica': row[7]
    }
    return pergunta

@app.route('/pergunta', methods=['POST'])
def get_pergunta():
    perguntas_usadas = request.json.get('usadas', [])
    pergunta = obter_pergunta_aleatoria(perguntas_usadas)
    if not pergunta:
        return jsonify({'erro': 'Sem perguntas disponíveis'}), 404
    random.shuffle(pergunta['alternativas'])
    return jsonify(pergunta)

@app.route('/verificar', methods=['POST'])
def verificar():
    dados = request.json
    id_pergunta = dados['id']
    resposta = dados['resposta']

    cursor = conn.cursor()
    cursor.execute("SELECT resposta_correta FROM perguntas WHERE id = ?", (id_pergunta,))
    row = cursor.fetchone()
    if row:
        correta = row[0]
        return jsonify({'correto': resposta == correta})
    return jsonify({'erro': 'Pergunta não encontrada'}), 404

@app.route('/dica/<int:pergunta_id>', methods=['GET'])
def get_dica(pergunta_id):
    cursor = conn.cursor()
    cursor.execute("SELECT dica FROM perguntas WHERE id = ?", (pergunta_id,))
    row = cursor.fetchone()
    if row:
        return jsonify({'dica': row[0]})
    return jsonify({'erro': 'Dica não encontrada'}), 404

@app.route('/-2/<int:pergunta_id>', methods=['GET'])
def remover_alternativas(pergunta_id):
    cursor = conn.cursor()
    cursor.execute("SELECT alternativa1, alternativa2, alternativa3, alternativa4, resposta_correta FROM perguntas WHERE id = ?", (pergunta_id,))
    row = cursor.fetchone()
    if row:
        alternativas = list(row[:4])
        correta = row[4]
        incorretas = [alt for alt in alternativas if alt != correta]
        removidas = random.sample(incorretas, 2)
        return jsonify({'removidas': removidas})
    return jsonify({'erro': 'Pergunta não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
