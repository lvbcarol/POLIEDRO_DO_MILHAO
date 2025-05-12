from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.db import get_db
import sqlite3

tentativas_bp = Blueprint("tentativas", __name__)

@tentativas_bp.route("/", methods=["POST"])
@jwt_required()
def registrar_nova_tentativa():
    id_usuario = get_jwt_identity() # Obtém o ID do usuário do token JWT
    data = request.get_json()
    valor_total = data.get("valor_total")

    if valor_total is None:
        return jsonify({"message": "Valor total é obrigatório"}), 400
    
    if not isinstance(valor_total, int):
        return jsonify({"message": "Valor total deve ser um número inteiro"}), 400

    db = get_db()
    try:
        cursor = db.execute("""
            INSERT INTO tentativas (ID_usuario, valor_total)
            VALUES (?, ?)
        """, (id_usuario, valor_total))
        db.commit()
        tentativa_id = cursor.lastrowid
        return jsonify({"message": "Tentativa registrada com sucesso!", "ID_tentativa": tentativa_id}), 201
    except Exception as e:
        return jsonify({"message": "Erro ao registrar tentativa", "error": str(e)}), 500

@tentativas_bp.route("/minhas", methods=["GET"])
@jwt_required()
def buscar_minhas_tentativas():
    id_usuario = get_jwt_identity()
    db = get_db()
    try:
        tentativas_rows = db.execute("SELECT * FROM tentativas WHERE ID_usuario = ? ORDER BY data_tentativa DESC", (id_usuario,)).fetchall()
        tentativas = [dict(row) for row in tentativas_rows]
        return jsonify(tentativas), 200
    except Exception as e:
        return jsonify({"message": "Erro ao buscar tentativas", "error": str(e)}), 500

# Opcional: Endpoint para buscar todas as tentativas (admin)
# @tentativas_bp.route("/", methods=["GET"])
# @jwt_required() # Adicionar verificação de admin se necessário
# def buscar_todas_tentativas():
#     db = get_db()
#     try:
#         tentativas_rows = db.execute("SELECT t.*, u.nickname FROM tentativas t JOIN usuarios u ON t.ID_usuario = u.ID_usuario ORDER BY t.data_tentativa DESC").fetchall()
#         tentativas = [dict(row) for row in tentativas_rows]
#         return jsonify(tentativas), 200
#     except Exception as e:
#         return jsonify({"message": "Erro ao buscar todas as tentativas", "error": str(e)}), 500

