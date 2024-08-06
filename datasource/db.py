import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()