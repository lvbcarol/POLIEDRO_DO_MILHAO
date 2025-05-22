from app import db

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class JogoRepository:
    def criar_jogo(self, dados):
        novo_jogo = Jogo(nome=dados['nome'])
        db.session.add(novo_jogo)
        db.session.commit()
        return novo_jogo

    def listar_jogos(self):
        return Jogo.query.all()
