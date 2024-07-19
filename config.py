import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, 'sqlite:///movie.db')

class ConfigDB:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movie.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False