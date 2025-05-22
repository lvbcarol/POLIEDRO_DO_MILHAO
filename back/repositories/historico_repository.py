from app import db

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200))

class HistoricoRepository:
    def adicionar_historico(self, dados):
        novo_historico = Historico(
            usuario_id=dados['usuario_id'],
            descricao=dados['descricao']
        )
        db.session.add(novo_historico)
        db.session.commit()
        return novo_historico

    def listar_por_usuario(self, usuario_id):
        return Historico.query.filter_by(usuario_id=usuario_id).all()
