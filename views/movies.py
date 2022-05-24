from flask_restx import Resource, Namespace
from implemented import movies_service
from flask import request, jsonify
from dao.model.movies import MoviesSchema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):

        year = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')

        if year:
            movies = movies_service.get_by_year(year)
        elif director_id:
            movies = movies_service.get_by_director(director_id)
        elif genre_id:
            movies = movies_service.get_by_genre(genre_id)
        else:
            movies = movies_service.get_all()

        result = MoviesSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        data = request.get_json()
        movies_id = data['id']
        movies_service.create(data)
        response = jsonify()
        response.status_code = 201
        response.headers['locations'] = f'movies/{movies_id}'

        return response


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        movie = movies_service.get_one(mid)
        result = MoviesSchema().dump(movie)
        return result, 200

    def put(self, mid):
        data = request.get_json()
        movies_service.update(data, mid)
        return '', 204

    def patch(self, mid):
        data = request.get_json()
        movies_service.update_part(data, mid)
        return '', 204

    def delete(self, mid):
        movies_service.delete(mid)
        return '', 204

