from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.db import get_db
import sqlite3

questao_bp = Blueprint("questao", __name__)

@questao_bp.route("/", methods=["POST"])
def adicionar_questao():
    data = request.get_json()
    # O ID_questao é AUTOINCREMENT, não precisa ser passado no request
    # id_questao = data.get("id_questao")
    enunciado = data.get("enunciado")
    alternativaA = data.get("alternativaA")
    alternativaB = data.get("alternativaB")
    alternativaC = data.get("alternativaC")
    alternativaD = data.get("alternativaD")
    resposta_correta = data.get("resposta_correta")
    dica = data.get("dica")
    valor = data.get("valor")
    nivel_dificuldade = data.get("nivel_dificuldade")

    if not all([enunciado, alternativaA, alternativaB, alternativaC, alternativaD, resposta_correta, dica, valor, nivel_dificuldade]):
        return jsonify({"message": "Campos obrigatórios da questão estão faltando"}), 400
    
    if resposta_correta.upper() not in ["A", "B", "C", "D"]:
        return jsonify({"message": "Resposta correta deve ser A, B, C ou D"}), 400

    db = get_db()
    try:
        cursor = db.execute("""
            INSERT INTO questoes (
                enunciado, alternativaA, alternativaB, alternativaC,
                alternativaD, resposta_correta, dica, valor, nivel_dificuldade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (enunciado, alternativaA, alternativaB, alternativaC, alternativaD, resposta_correta.upper(), dica, valor, nivel_dificuldade))
        db.commit()
        new_questao_id = cursor.lastrowid
        return jsonify({"message": "Questão adicionada com sucesso!", "ID_questao": new_questao_id}), 201
    except Exception as e:
        return jsonify({"message": "Erro ao adicionar questão", "error": str(e)}), 500

def buscar_questao_para_editar(id_questao):
    db = get_db()
    try:
        questao_row = db.execute("SELECT * FROM questoes WHERE ID_questao = ?", (id_questao,)).fetchone()
        if questao_row:
            return True
        else:
            return False
    except Exception as e:
        return False

@questao_bp.route("/", methods=["PUT"])
def editar_questao():
    data = request.get_json()
    # O ID_questao é AUTOINCREMENT, não precisa ser passado no request
    id_questao = data.get("ID_questao")
    print(id_questao)

    if not buscar_questao_para_editar(id_questao):
        return jsonify({"message": "Questão não encontrada!"}), 400

    enunciado = data.get("nova_enunciado")
    alternativaA = data.get("nova_alternativaA")
    alternativaB = data.get("nova_alternativaB")
    alternativaC = data.get("nova_alternativaC")
    alternativaD = data.get("nova_alternativaD")
    resposta_correta = data.get("nova_resposta_correta")
    dica = data.get("nova_dica")
    valor = data.get("nova_valor")
    nivel_dificuldade = data.get("novo_nivel_dificuldade")

    valores = []
    for valor in [enunciado, alternativaA, alternativaB, alternativaC, alternativaD, resposta_correta, dica, valor, nivel_dificuldade, id_questao]:
        if valor is not None:
            valores.append(valor)
    if not any(valores):
        return jsonify({"message": "Campos obrigatórios da questão estão faltando"}), 400
    
    if resposta_correta is not None and resposta_correta.upper() not in ["A", "B", "C", "D"]:
        return jsonify({"message": "Resposta correta deve ser A, B, C ou D"}), 400

    db = get_db()
    updates = tuple(valores)
    try:
        cursor = db.execute(f"""
            UPDATE questoes 
            SET (
                {'enunciado = ?,' if enunciado is not None else ''} 
                {'alternativaA = ?,' if alternativaA is not None else ''}
                {'alternativaB = ?,'if alternativaB is not None else ''}
                {'alternativaC = ?, 'if alternativaC is not None else ''}
                {'alternativaD = ?,'if alternativaD is not None else ''}
                {'resposta_correta = ?,' if resposta_correta is not None else ''}
                {'dica = ?,'if dica is not None else ''} 
                {'valor = ?,'if valor is not None else ''} 
                {'nivel_dificuldade = ?,'if nivel_dificuldade is not None else ''}
                )
            WHERE ID_questao = ?
        """, updates)
        db.commit()
        new_questao_id = cursor.lastrowid
        return jsonify({"message": "Questão adicionada com sucesso!", "ID_questao": new_questao_id}), 201
    except Exception as e:
        return jsonify({"message": "Erro ao adicionar questão", "error": str(e)}), 500


@questao_bp.route("/", methods=["GET"])
def listar_questoes():
    db = get_db()
    try:
        questoes_rows = db.execute("SELECT * FROM questoes").fetchall()
        questoes = [dict(row) for row in questoes_rows]
        return jsonify(questoes), 200
    except Exception as e:
        return jsonify({"message": "Erro ao buscar questões", "error": str(e)}), 500

@questao_bp.route("/<int:id_questao>", methods=["GET"])
def buscar_questao(id_questao):
    db = get_db()
    try:
        questao_row = db.execute("SELECT * FROM questoes WHERE ID_questao = ?", (id_questao,)).fetchone()
        if questao_row:
            return jsonify(dict(questao_row)), 200
        else:
            return jsonify({"message": "Questão não encontrada"}), 404
    except Exception as e:
        return jsonify({"message": "Erro ao buscar questão", "error": str(e)}), 500

@questao_bp.route("/check_answer", methods=["POST"]) # Geralmente verificar resposta é parte de um fluxo autenticado
def verificar_resposta():
    data = request.get_json()
    id_questao = data.get("id_questao")
    resposta_usuario = data.get("resposta_usuario") # Espera-se "A", "B", "C" ou "D"

    if not id_questao or not resposta_usuario:
        return jsonify({"message": "ID da questão e resposta do usuário são obrigatórios"}), 400
    
    if resposta_usuario.upper() not in ["A", "B", "C", "D"]:
        return jsonify({"message": "Resposta do usuário deve ser A, B, C ou D"}), 400

    db = get_db()
    try:
        questao_row = db.execute("SELECT resposta_correta FROM questoes WHERE ID_questao = ?", (id_questao,)).fetchone()
        if not questao_row:
            return jsonify({"message": "Questão não encontrada"}), 404
        
        correto = (resposta_usuario.upper() == questao_row["resposta_correta"].upper())
        return jsonify({"correto": correto}), 200
    except Exception as e:
        return jsonify({"message": "Erro ao verificar resposta", "error": str(e)}), 500

