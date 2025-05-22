from flask import Blueprint, request, jsonify
from usecases.historico_usecase import HistoricoUseCase
from repositories.historico_repository import HistoricoRepository
from flask_jwt_extended import jwt_required, get_jwt_identity

historico_bp = Blueprint('historico', __name__)
historico_usecase = HistoricoUseCase(HistoricoRepository())

@historico_bp.route('/historico', methods=['POST'])
@jwt_required()
def adicionar_historico():
    usuario_id = get_jwt_identity()
    dados = request.json
    dados['usuario_id'] = usuario_id
    historico = historico_usecase.adicionar_historico(dados)
    return jsonify({'id': historico.id, 'descricao': historico.descricao}), 201

@historico_bp.route('/historico', methods=['GET'])
@jwt_required()
def listar_historico():
    usuario_id = get_jwt_identity()
    historicos = historico_usecase.listar_historico_usuario(usuario_id)
    return jsonify([{'id': h.id, 'descricao': h.descricao} for h in historicos])
