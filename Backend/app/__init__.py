from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from .utils import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    JWTManager(app)
    db.init_app(app)

    with app.app_context():
        db.init_db_command()

    from .routes.auth import auth_bp
    from .routes.questao import questao_bp
    from .routes.tentativas import tentativas_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(questao_bp, url_prefix="/api/questoes")
    app.register_blueprint(tentativas_bp, url_prefix="/api/tentativas")

    return app

