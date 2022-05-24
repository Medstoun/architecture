from dao.model.genres import Genres, GenresSchema


class GenresDAO:
    def __int__(self, session):
        self.session = session

    def get_all_genres(self):
        genres = Genres.query.all()
        return genres

    def get_one(self, gid):
        genre = Genres.query.get(gid)
        return genre
