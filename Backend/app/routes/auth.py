from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.utils.db import get_db
import sqlite3

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    nickname = data.get("nickname")
    senha = data.get("senha")

    if not nickname or not senha:
        return jsonify({"message": "Nickname e senha são obrigatórios"}), 400

    db = get_db()
    try:
        cursor = db.execute(
            "INSERT INTO usuarios (nickname, senha) VALUES (?, ?)",
            (nickname, generate_password_hash(senha))
        )
        db.commit()
        user_id = cursor.lastrowid
        return jsonify({"message": "Usuário registrado com sucesso!", "ID_usuario": user_id}), 201
    except sqlite3.IntegrityError: # Nickname já existe
        return jsonify({"message": "Nickname já cadastrado"}), 409
    except Exception as e:
        return jsonify({"message": "Erro ao registrar usuário", "error": str(e)}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data.get("nickname")
    senha = data.get("senha")

    if not nickname or not senha:
        return jsonify({"message": "Nickname e senha são obrigatórios"}), 400

    db = get_db()
    user_row = db.execute(
        "SELECT * FROM usuarios WHERE nickname = ?", (nickname,)
    ).fetchone()

    if user_row and check_password_hash(user_row["senha"], senha):
        # Corrigido: Converter ID_usuario para string para o JWT identity
        access_token = create_access_token(identity=str(user_row["ID_usuario"]))
        return jsonify(access_token=access_token, ID_usuario=user_row["ID_usuario"], nickname=user_row["nickname"]), 200
    else:
        return jsonify({"message": "Nickname ou senha inválidos"}), 401

