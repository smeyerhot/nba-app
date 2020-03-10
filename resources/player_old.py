# from flask import Flask, jsonify, request, Response
from flask import Blueprint, Response, request


from database.models import Player

players = Blueprint('players', __name__)

# @app.route('/players')
@players.route('/players')
def get_players():
    players = Player.objects().to_json()
    return Response(players, mimetype="application/json", status=200)


# @app.route('/players', methods=['POST'])
@players.route('/players', methods=['POST'])
def add_movie():
    body = request.get_json()
    print(type(body))
    player = Player(**body).save()
    id = player.id 
    return {'id': str(id)}, 200

# @app.route('/players/<int:index>', methods=['PUT']) \\ variable name accepted as a keyword argument <converter:variable_name>.
# def update_player(index):
#     player = request.get_json()
#     players[index] = player
#     return jsonify(players[index]), 200

# @app.route('/players/<id>', methods=['PUT'])
@players.route('/players/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Player.objects.get(id=id).update(**body)
    return '', 200

# @app.route('/players/<id>', methods=['DELETE'])
@players.route('/players/<id>', methods=['DELETE'])
def delete_movie(id):
    player = Player.objects.get(id=id).delete()
    return '', 200

# @app.route('/players/<id>')
@players.route('/players/<id>')
def get_movie(id):
    players = Player.objects.get(id=id).to_json()
    return Response(players, mimetype="application/json", status=200)
