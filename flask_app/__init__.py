from flask import Flask

def create_app():
    app = Flask(__name__)

    app.secret_key = '236263264bb0232'

    from .routes import main
    app.register_blueprint(main)
    return app

