import os
from datasource.db import db
from server.instance import server
from domain.movie import MovieModel

app = server.app

@app.before_request
def create_tables():
    if not os.path.exists('Outsera/instance/movie.db'):
        app.before_request_funcs[None].remove(create_tables)
        db.create_all()
        MovieModel.persist_csv_to_table()

if __name__ == "__main__":
    db.init_app(app)
    server.run()
    