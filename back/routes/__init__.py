# Onde define os endpoints do API

from controllers.usuario_controller import usuario_bp
from controllers.jogo_controller import jogo_bp
from controllers.historico_controller import historico_bp

def register_routes(app):
    app.register_blueprint(usuario_bp, url_prefix='/api')
    app.register_blueprint(jogo_bp, url_prefix='/api')
    app.register_blueprint(historico_bp, url_prefix='/api')


# from controllers import usuario_controller, jogo_controller, historico_controller

# def register_routes(app):
#     app.register_blueprint(usuario_controller.bp)
#     app.register_blueprint(jogo_controller.bp)
#     app.register_blueprint(historico_controller.bp)
