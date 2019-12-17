from src.Exceptions.GenreExceptions import InvalidGenreDescription, DeleteException, InsertException
from src.util.Constants import Constants


class GenreService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        genres = []
        for x in self.repository.get_all():
            genres.append({
                'value': x.id,
                'label': x.description
            })
        return genres

    def insert(self, genre):
        try:
            self.validate(genre)
            self.repository.insert(genre)
            return 'Genero Inserida com sucesso'
        except InvalidGenreDescription as e:
            return e
        except InsertException as e:
            return e

    def delete(self, id):
        try:
            if id is None:
                raise DeleteException
            if not isinstance(id, int):
                raise DeleteException
            self.repository.delete(id)
            return 'Genero deletado com sucesso'
        except DeleteException as e:
            return e

    def validate(self, publisher):
        if publisher.description is None:
            raise InvalidGenreDescription
        if publisher.description.strip() == '':
            raise InvalidGenreDescription
        if len(publisher.description) <= 3:
            raise InvalidGenreDescription
