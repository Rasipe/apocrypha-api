from src.Exceptions.BookExceptions import InvalidBookTitle, DeleteException, InvalidPublisher, InvalidGenre, InsertException, UpdateException


class BookService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        books = []
        for x in self.repository.get_all():
            books.append({
                'id': x.id,
                'title': x.title,
                'pages': x.pages,
                'value_mulct': x.value_mulct,
                'genre': x.genre.description,
                'publisher': x.publisher.name,
                'collection': x.collection.name
            })
        return books

    def get(self, book_id):
        book = self.repository.get(book_id)
        return {
                'id': book.id,
                'title': book.title,
                'pages': book.pages,
                'value_mulct': book.value_mulct,
                'genre': book.genre.description,
                'publisher': book.publisher.name,
                'collection': book.collection.name
            }

    def insert(self, book):
        try:
            self.validate(book)
            if not hasattr(book.collection, 'id'):
                from src.model.Collection import Collection
                book.collection = Collection(0, '')
            self.repository.insert(book)
            return 'Livro inserido com sucesso'
        except InvalidBookTitle as e:
            return e
        except InvalidPublisher as e:
            return e
        except InvalidGenre as e:
            return e
        except InsertException as e:
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
        except UpdateException as e:
            return e

    def delete(self, id):
        try:
            if id is None:
                raise DeleteException
            self.repository.delete(id)
            return 'Livro deletado com sucesso'
        except DeleteException as e:
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
