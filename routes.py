from flask import jsonify, Blueprint
from domain.movie import MovieModel

bp_movies = Blueprint('movies', __name__)

@bp_movies.route('/movies', methods=['GET'])
def get_movies():
    movies = MovieModel.get_all_movies()

    return jsonify([{
        "year": movie.year,
        "title": movie.title,
        "studios": movie.studios,
        "producers": movie.producers,
        "winner": movie.winner
    } for movie in movies]), 200


@bp_movies.route('/producers', methods=['GET'])
def get_producers_winners():
    winners = MovieModel.get_all_winners()
    producers_dict = {}
    for movie in winners:
        producers = [producer.strip() for producer in movie.producers.split(',')]
        for producer in producers:
            if producer not in producers_dict:
                producers_dict[producer] = []
            producers_dict[producer].append(movie.year)
    
    min_interval_producers = []
    max_interval_producers = []

    for producer, years in producers_dict.items():
        if len(years) > 1:
            years.sort()
            intervals = [years[i+1] - years[i] for i in range(len(years) - 1)]
            min_interval = min(intervals)
            max_interval = max(intervals)
            min_interval_index = intervals.index(min_interval)
            max_interval_index = intervals.index(max_interval)
            
            min_interval_producers.append({
                "producer": producer,
                "interval": min_interval,
                "previousWin": years[min_interval_index],
                "followingWin": years[min_interval_index + 1]
            })
            max_interval_producers.append({
                "producer": producer,
                "interval": max_interval,
                "previousWin": years[max_interval_index],
                "followingWin": years[max_interval_index + 1]
            })

    min_interval_producers = min(min_interval_producers, key=lambda x: x['interval'])
    max_interval_producers = max(max_interval_producers, key=lambda x: x['interval'])

    return jsonify({
        "min": min_interval_producers,
        "max": max_interval_producers
    })


