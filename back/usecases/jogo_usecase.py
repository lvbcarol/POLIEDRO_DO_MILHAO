from repositories.jogo_repository import JogoRepository

class JogoUseCase:
    def __init__(self, jogo_repository: JogoRepository):
        self.jogo_repository = jogo_repository

    def criar_jogo(self, dados):
        return self.jogo_repository.criar_jogo(dados)

    def listar_jogos(self):
        return self.jogo_repository.listar_jogos()
