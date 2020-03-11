from flask import Blueprint, Response, request, jsonify
from database.models import Player  
from flask_restful import Resource




players = Blueprint('players', __name__)

@players.route('/', methods=['GET'])
def index():
    players = Player.objects().to_json()
    return '''
<html>
    <head>
        <title> Players </title>
    </head>
    <body>
        <h1> Hello, ''' + players + '''!</h1>
    </body>
</html>'''


class PlayersApi(Resource):
    def get(self):
        players = Player.objects().to_json()
        print(f'players:{players}')
        return Response(players, mimetype='application/json', status=200)

    def post(self):
        body = request.get_json()
        player = Player(**body).save()
        id = player.id
        return {'id': str(id)}

class PlayerApi(Resource):
    def put(self, id):
        body = request.get_json()
        Player.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        player = Player.objects.get(id=id).delete()
        return '', 200
    
    def get(self, id):
        players = Player.objects.get(id=id).to_json()
        return Response(players, mimetype="application/json", status=200)

