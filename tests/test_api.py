import pytest
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from datasource.db import db

from server.instance import Server
from domain.movie import MovieModel

server = Server()
db.init_app(server.app)

@pytest.fixture()
def app():
    with server.app.app_context():
        db.create_all()

    yield server.app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def init_database():
    with server.app.app_context():
        db.create_all()

        MovieModel.persist_csv_to_table()

        yield db  
        db.session.remove()
        db.drop_all()


def test_endpoint_movies(client, init_database):
    response = client.get('/movies')
    assert response.status_code == 200

    data = response.get_json()
    assert 'producers' in data[0]
    assert 'studios' in data[0]
    assert 'title' in data[0]
    assert 'winner' in data[0]


def test_endpoint_producers(client, init_database):
    response = client.get('/producers')
    assert response.status_code == 200

    data = response.get_json()    
    assert len(data) > 0
 