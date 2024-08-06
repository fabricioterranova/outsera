from flask import Flask
from config import ConfigDB

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(ConfigDB)

        from routes import bp_movies
        self.app.register_blueprint(bp_movies)

    def run(self):
        url = '0.0.0.0'
        self.app.run(host=url, 
                     port=5000)
        

server = Server()