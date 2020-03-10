from flask import Flask
from database.db import initialize_db
from resources.player import players

app = Flask(__name__)


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
app.register_blueprint(players)

app.run()
