import pytest

from unittest.mock import MagicMock
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService
from setup_db import db

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    extra = Movie(id=1,
    title='extra',
    description='description_1',
    trailer='trailer_1',
    year=1996,
    rating=1,
    genre_id=1,
    director_id=1)

    alf = Movie(id=2,
    title='alf',
    description='description_2',
    trailer='trailer_2',
    year=2000,
    rating=2,
    genre_id=2,
    director_id=2)
    
    mamma_mia = Movie(id=3,
    title='mamma_mia',
    description='description_3',
    trailer='trailer_3',
    year=2004,
    rating=3',
    genre_id=3,
    director_id=3)

    movie_dao.get_one = MagicMock(return_value=extra)
    movie_dao.get_all = MagicMock(return_value=[extra, alf, mamma_mia])
    movie_dao.create = MagicMock(return_value=Director(id=2, title='Friends'))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)
    
    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
    
    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0
    
    def test_create(self):
        movie_d = {
            'title': 'Friends'
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None
    
    def test_delete(self):
        movie = self.movie_service.delete(1)
        assert movie.get(1) is None
    
    def test_update(self):
        movie_d = {
            'id': 1,
            'title': 'Forest_Gump'
        }
        movie = self.movie_service.update(movie_d)
        assert movie.get(1) == 'Forest_Gump'