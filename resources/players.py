from flask import Response, request

from database.models import Player

class PlayersApi(Resource):
    def get(self):
        players = Player.objects.to_json()
        print(f'players:{players}')
        return Response(players, mimetype='application/json', status=200)

    def post(self):
        body = request.get_json()