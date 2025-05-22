# Lógica do negócio (regras do sistema 'o que fazer')

from repositories.usuario_repository import UsuarioRepository

class UsuarioUseCase:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    def criar_usuario(self, dados):
        return self.usuario_repository.criar_usuario(dados)

    def autenticar_usuario(self, email, senha):
        return self.usuario_repository.autenticar_usuario(email, senha)
