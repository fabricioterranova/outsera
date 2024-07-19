import pandas as pd
from datasource.db import db

class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    studios = db.Column(db.String)
    producers = db.Column(db.String, nullable=False)
    winner = db.Column(db.String, nullable=True)

    def __init__(self, year: int, title: str, studios: str, 
                 producers: str, winner: str) -> None:
        self.year = year
        self.title = title
        self.studios = studios
        self.producers = producers
        self.winner = winner

    def __repr__(self) -> str:
        return f"MovieModel (year:{self.year}, title:{self.title}, studios:{self.studios}, producers:{self.producers}, winner: {self.winner}) "
    
    def json(self) -> dict:
        return {
            'year': self.year,
            'title': self.title,
            'studios': self.studios,
            'producers': self.producers,
            'winner': self.winner
        }
    
    @classmethod
    def get_all_movies(cls):
        return cls.query.all()
    
    @classmethod
    def get_all_winners(cls):
        return cls.query.filter_by(winner="yes").all()
    
    @classmethod
    def persist_csv_to_table(cls):

        path = 'Outsera/datasource/movielist.csv'
        data_csv = pd.read_csv(path, sep=';')

        for _, row in data_csv.iterrows():
            movie = MovieModel(
                year=row['year'],
                title=row['title'],
                studios=row['studios'],
                producers=row['producers'],
                winner=row['winner']
            )
            db.session.add(movie)
        db.session.commit()


    @classmethod
    def persist_csv_to_table_for_test(cls):
        path = 'Outsera/datasource/movielist.csv'
        data_csv = pd.read_csv(path, sep=';')

        for _, row in data_csv.iterrows():
            movie = MovieModel(
                year=row['year'],
                title=row['title'],
                studios=row['studios'],
                producers=row['producers'],
                winner=row['winner']
            )
            db.session.add(movie)
        db.session.commit()