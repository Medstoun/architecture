from dao.model.movies import Movies, MoviesSchema


class MoviesDAO:
    def __int__(self, session):
        self.session = session

    def get_all_movies(self):
        movies = Movies.query.all()
        return movies

    def get_one(self, mid):
        movie = Movies.query.get(mid)
        return movie

    def get_by_year(self, year):
        movie = Movies.query.filter(Movies.year == year).all()
        return movie

    def get_by_genre(self, genre_id):
        movie = Movies.query.filter(Movies.genre_id == genre_id).all()
        return movie

    def get_by_director(self, director_id):
        movie = Movies.query.filter(Movies.director_id == director_id).all()
        return movie

    def create(self, data):
        movie = Movies(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
        self.session.close()
