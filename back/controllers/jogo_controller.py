from flask import Blueprint, request, jsonify
from usecases.jogo_usecase import JogoUseCase
from repositories.jogo_repository import JogoRepository

jogo_bp = Blueprint('jogo', __name__)
jogo_usecase = JogoUseCase(JogoRepository())

@jogo_bp.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.json
    jogo = jogo_usecase.criar_jogo(dados)
    return jsonify({'id': jogo.id, 'nome': jogo.nome}), 201

@jogo_bp.route('/jogos', methods=['GET'])
def listar_jogos():
    jogos = jogo_usecase.listar_jogos()
    return jsonify([{'id': j.id, 'nome': j.nome} for j in jogos])
