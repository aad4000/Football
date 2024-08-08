from flask import request, jsonify
from .player_service import (
    insert_player, select_team, count_players_by_position,
    get_all_players_sorted_by_apt, get_player_with_highest_apt,
    get_player_with_lowest_avg
)
from .player_schema import validate_player_data

def add_player():
    data = request.json
    is_valid, validated_data = validate_player_data(data)
    if not is_valid:
        return jsonify({'errors': validated_data}), 400
    insert_player(
        validated_data['first_name'],
        validated_data['last_name'],
        validated_data['apt'],
        validated_data['set'],
        validated_data['position'],
        validated_data['national_association']
    )
    return jsonify({'message': 'Player added successfully'}), 201

def get_team():
    num_players = int(request.args.get('num_players', 10))
    team = select_team(num_players)
    return jsonify(team), 200

def count_by_position():
    counts = count_players_by_position()
    return jsonify(counts), 200

def sorted_players():
    players = get_all_players_sorted_by_apt()
    return jsonify(players), 200

def highest_apt():
    player = get_player_with_highest_apt()
    return jsonify(player), 200

def lowest_avg():
    player = get_player_with_lowest_avg()
    return jsonify(player), 200
