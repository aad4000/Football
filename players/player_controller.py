from flask import Blueprint, request, jsonify
from players.player_service import (
    insert_player, select_team, count_players_by_position,
    get_all_players_sorted_by_apt, get_player_with_highest_apt,
    get_player_with_lowest_avg
)

player_blueprint = Blueprint('player_blueprint', __name__)

@player_blueprint.route('/add_player', methods=['POST'])
def add_player():
    data = request.json
    insert_player(
        data['first_name'],
        data['last_name'],
        data['apt'],
        data['set'],
        data['position'],
        data['national_association']
    )
    return jsonify({'message': 'Player added successfully'}), 201

@player_blueprint.route('/select_team', methods=['GET'])
def get_team():
    num_players = int(request.args.get('num_players', 10))
    team = select_team(num_players)
    return jsonify(team), 200

@player_blueprint.route('/count_players_by_position', methods=['GET'])
def count_by_position():
    counts = count_players_by_position()
    return jsonify(counts), 200

@player_blueprint.route('/sorted_players', methods=['GET'])
def sorted_players():
    players = get_all_players_sorted_by_apt()
    return jsonify(players), 200

@player_blueprint.route('/highest_apt', methods=['GET'])
def highest_apt():
    player = get_player_with_highest_apt()
    return jsonify(player), 200

@player_blueprint.route('/lowest_avg', methods=['GET'])
def lowest_avg():
    player = get_player_with_lowest_avg()
    return jsonify(player), 200
