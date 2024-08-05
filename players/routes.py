from flask import Flask
from players.player_controller import player_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(player_blueprint, url_prefix='/players')
    return app
