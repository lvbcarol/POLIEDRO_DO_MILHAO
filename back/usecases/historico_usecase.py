from repositories.historico_repository import HistoricoRepository

class HistoricoUseCase:
    def __init__(self, historico_repository: HistoricoRepository):
        self.historico_repository = historico_repository

    def adicionar_historico(self, dados):
        return self.historico_repository.adicionar_historico(dados)

    def listar_historico_usuario(self, usuario_id):
        return self.historico_repository.listar_por_usuario(usuario_id)
