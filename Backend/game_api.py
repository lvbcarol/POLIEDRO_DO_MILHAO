from flask import Flask, request, jsonify
import sqlite3
import random

app = Flask(__name__)

# Tabela perguntas já deve estar criada conforme conversamos, com colunas:
# id, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, correta, dica

@app.route('/pergunta', methods=['GET'])
def get_pergunta():
    conn = sqlite3.connect('banco_jogo.db')
    cursor = conn.cursor()

    # Excluir IDs já respondidos (enviados via query string)
    respondidas = request.args.get('respondidas', '')
    excluidas = tuple(map(int, respondidas.split(','))) if respondidas else (-1,)

    cursor.execute(f'''
        SELECT id, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, dica
        FROM perguntas
        WHERE id NOT IN ({','.join(['?'] * len(excluidas))})
        ORDER BY RANDOM()
        LIMIT 1
    ''', excluidas)

    row = cursor.fetchone()
    conn.close()

    if row:
        pergunta = {
            'id': row[0],
            'enunciado': row[1],
            'alternativas': [
                {'letra': 'A', 'texto': row[2]},
                {'letra': 'B', 'texto': row[3]},
                {'letra': 'C', 'texto': row[4]},
                {'letra': 'D', 'texto': row[5]}
            ],
            'dica': row[6]
        }
        return jsonify(pergunta)
    else:
        return jsonify({'fim': True})  # Não há mais perguntas

@app.route('/verificar_resposta', methods=['POST'])
def verificar_resposta():
    dados = request.json
    id_pergunta = dados.get('id')
    resposta = dados.get('resposta')

    conn = sqlite3.connect('banco_jogo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT correta FROM perguntas WHERE id = ?', (id_pergunta,))
    correta = cursor.fetchone()
    conn.close()

    if correta:
        return jsonify({'correta': resposta == correta[0]})
    else:
        return jsonify({'erro': 'Pergunta não encontrada'}), 404

@app.route('/ajuda/tirar_duas', methods=['POST'])
def ajuda_tirar_duas():
    dados = request.json
    id_pergunta = dados.get('id')

    conn = sqlite3.connect('banco_jogo.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT alternativa_a, alternativa_b, alternativa_c, alternativa_d, correta
        FROM perguntas WHERE id = ?
    ''', (id_pergunta,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({'erro': 'Pergunta não encontrada'}), 404

    alternativas = {
        'A': row[0],
        'B': row[1],
        'C': row[2],
        'D': row[3],
    }
    correta = row[4]
    
    erradas = [letra for letra in alternativas if letra != correta]
    eliminadas = random.sample(erradas, 2)

    return jsonify({'eliminadas': eliminadas})

@app.route('/ajuda/dica/<int:id>', methods=['GET'])
def ajuda_dica(id):
    conn = sqlite3.connect('banco_jogo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT dica FROM perguntas WHERE id = ?', (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({'dica': row[0]})
    return jsonify({'erro': 'Dica não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
