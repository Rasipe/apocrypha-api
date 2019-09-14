from Exceptions.BookExceptions import InvalidBookTitle
from Exceptions.BookExceptions import InvalidPublisher
from Exceptions.BookExceptions import InvalidGenre
from Exceptions.BookExceptions import InvalidId


class BookService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def insert(self, book):
        try:
            self.validate(book)
            if not hasattr(book.collection, 'id'):
                from model.Collection import Collection
                book.collection = Collection(0, '')
            self.repository.insert(book)
            return 'Livro inserido com sucesso'
        except InvalidBookTitle as e:
            return e
        except InvalidPublisher as e:
            return e
        except InvalidGenre as e:
            return e

    def update(self, book):
        try:
            self.validate(book)
            self.repository.update(book)
            return 'Livro atualizado com sucesso'
        except InvalidBookTitle as e:
            return e
        except InvalidPublisher as e:
            return e
        except InvalidGenre as e:
            return e

    def delete(self, id):
        try:
            if id is None:
                raise InvalidId
            if not isinstance(id, int):
                raise InvalidId
            self.repository.delete(id)
            return 'Livro deletado com sucesso'
        except InvalidId as e:
            return e

    def validate(self, book):
        if book.title is None:
            raise InvalidBookTitle
        if book.title.strip() == '':
            raise InvalidBookTitle
        if len(book.title) <= 3:
            raise InvalidBookTitle
        if not hasattr(book.publisher, 'id'):
            raise InvalidPublisher
        if not hasattr(book.genre, 'id'):
            raise InvalidGenre