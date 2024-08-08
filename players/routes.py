from flask import Flask
from .player_controller import (
    add_player, get_team, count_by_position,
    sorted_players, highest_apt, lowest_avg
)

def create_app():
    app = Flask(__name__)
    
    app.route('/players/add_player', methods=['POST'])(add_player)
    app.route('/players/select_team', methods=['GET'])(get_team)
    app.route('/players/count_players_by_position', methods=['GET'])(count_by_position)
    app.route('/players/sorted_players', methods=['GET'])(sorted_players)
    app.route('/players/highest_apt', methods=['GET'])(highest_apt)
    app.route('/players/lowest_avg', methods=['GET'])(lowest_avg)

    return app
