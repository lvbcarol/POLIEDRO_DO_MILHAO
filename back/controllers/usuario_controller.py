from flask import Blueprint, request, jsonify
from repositories.usuario_repository import cadastrar_usuario_db

bp = Blueprint("usuario", __name__)

@bp.route("/cadastro", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()
    nickname = dados.get("nickname")
    senha = dados.get("senha")

    if not nickname or not senha:
        return jsonify({"mensagem": "Dados incompletos"}), 400

    try:
        cadastrar_usuario_db(nickname, senha)
        return jsonify({"mensagem": "Usuário cadastrado com sucesso"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500



# # Funções que respondem às requisições do API

# from flask import Blueprint, request, jsonify
# from usecases.usuario_usecase import UsuarioUseCase
# from repositories.usuario_repository import UsuarioRepository
# from flask_jwt_extended import create_access_token

# usuario_bp = Blueprint('usuario', __name__)
# usuario_usecase = UsuarioUseCase(UsuarioRepository())

# @usuario_bp.route('/usuarios', methods=['POST'])
# def criar_usuario():
#     dados = request.json
#     usuario = usuario_usecase.criar_usuario(dados)
#     return jsonify({'id': usuario.id, 'email': usuario.email}), 201

# @usuario_bp.route('/login', methods=['POST'])
# def login():
#     dados = request.json
#     usuario = usuario_usecase.autenticar_usuario(dados['email'], dados['senha'])
#     if usuario:
#         token = create_access_token(identity=usuario.id)
#         return jsonify({'token': token})
#     return jsonify({'erro': 'Credenciais inválidas'}), 401


# from flask import Blueprint, request, jsonify
# from repositories.usuario_repository import cadastrar_usuario_db

# bp = Blueprint("usuario", __name__)

# @bp.route("/cadastro", methods=["POST"])
# def cadastrar_usuario():
#     dados = request.get_json()
#     nickname = dados.get("nickname")
#     senha = dados.get("senha")

#     if not nickname or not senha:
#         return jsonify({"mensagem": "Dados incompletos"}), 400

#     try:
#         cadastrar_usuario_db(nickname, senha)
#         return jsonify({"mensagem": "Usuário cadastrado com sucesso"}), 201
#     except Exception as e:
#         return jsonify({"erro": str(e)}), 500
