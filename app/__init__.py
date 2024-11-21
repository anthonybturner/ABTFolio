from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='../client/build/static', template_folder='../client/build')

    # Register routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app