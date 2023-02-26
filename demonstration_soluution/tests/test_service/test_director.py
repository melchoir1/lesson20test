import pytest

from unittest.mock import MagicMock
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService
from setup_db import db

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    jonh = Director(id=1, name='jonh')
    kate = Director(id=2, name='kate')
    maxim = Director(id=3, name='maxim')

    director_dao.get_one = MagicMock(return_value=jonh)
    director_dao.get_all = MagicMock(return_value=[jonh, kate, maxim])
    director_dao.create = MagicMock(return_value=Director(id=2, name='Denis'))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None


#начал писать код 14.02 21:30
    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0
    
    def test_create(self):
        director_d = {
            'name': 'Denis'
        }
        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_delete(self):
        # self.director_service.delete(1)

        # self.director_service.delete(1)
        # director = self.director_service.get(1)
        # assert director is None

        director = self.director_service.delete(1)
        assert director.get(1) is None

    def test_update(self):
        director_d = {
            'id': 1,
            'name': 'Ivan'
        }
        director = self.director_service.update(director_d)
        assert director.get(1) == 'Ivan'
        
    