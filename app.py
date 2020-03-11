from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

from resources.players import players

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

# players = [
#     {
#         "name": "Lebron James",
#         "teams": ["Cavs","Heat","Lakers"],
#         "positions":["PG","SF","PF"],
#         "championships": 3    
#     },
#     {
#         "name": "Anthony Davis",
#         "teams": ["Pelicans","Lakers"],
#         "positions":["C","PF"],
#         "championships": 0    
#     },
#     {
#         "name": "Kawai Leonard",
#         "teams": ["Spurs", "Raptors", "Clippers"],
#         "positions":["SF"],
#         "championships": 2   
#     }
# ]

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/theorize'
}
initialize_db(app)
initialize_routes(api)

app.register_blueprint(players)

app.run()
