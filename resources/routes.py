from .players import PlayersApi, PlayerApi
from .auth import SignupApi

def initialize_routes(api):
    api.add_resource(PlayersApi, '/api/players')
    api.add_resource(PlayerApi, '/api/players/<id>')


    api.add_resource(SignupApi, '/api/auth/signup')