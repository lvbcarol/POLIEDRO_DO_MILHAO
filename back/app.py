from flask import Flask
from flask_cors import CORS
from controllers.usuario_controller import bp as usuario_bp

app = Flask(__name__)
CORS(app)  # ✅ Para liberar acesso via React Native Web

app.register_blueprint(usuario_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# Ponto de entrada do backend
# Local: back/app.py

# from flask import Flask
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
# from config import Config

# db = SQLAlchemy()
# jwt = JWTManager()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     CORS(app)

#     db.init_app(app)
#     jwt.init_app(app)

#     from routes import register_routes
#     register_routes(app)

#     return app


# from flask import Flask
# from flask_cors import CORS
# from back.routes import register_routes
# from back.database.init_db import criar_tabela

# def create_app():
#     app = Flask(__name__)
#     CORS(app)

#     criar_tabela()
#     register_routes(app)

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(host='0.0.0.0', port=5000, debug=True)