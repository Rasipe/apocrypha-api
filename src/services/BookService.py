from src.Exceptions.BookExceptions import InvalidBookTitle, DeleteException, InvalidPublisher, InvalidGenre, InsertException, UpdateException


class BookService:
    def __init__(self, repository):
        self.repository = repository

    def get_books_for_client(self):
        db_books = self.repository.get_all()
        books = []
        for db_book in db_books:
            quantity = db_book['quantity']
            if any(x['Id'] == db_book['book_id'] for x in books):
                continue
            book = {
                'Id': db_book['book_id'],
                'Title': db_book['title'],
                'Publisher': db_book['publisher_name'],
                'Genres': '',
                'Authors': '',
                'Available': True
            }
            if db_book['collection_id']:
                book['Collection'] = db_book['collection_name']
            books_by_book_id = list(filter(lambda x: x['book_id'] == db_book['book_id'], db_books))

            mapped_list = list(
                map(lambda x: x['genre_description'], books_by_book_id))
            for genre in mapped_list:
                if genre in book['Genres']:
                    continue
                if not book['Genres']:
                    book['Genres'] = genre
                    continue
                book['Genres'] += f', {genre}'

            mapped_list = list(
                map(lambda x: x['author_name'], books_by_book_id))
            for author in mapped_list:
                if author in book['Authors']:
                    continue
                if not book['Authors']:
                    book['Authors'] = author
                    continue
                book['Authors'] += f', {author}'

            loans = self.repository.get_count_loans(book['Id'])

            unavailable = loans
            if quantity == unavailable:
                book['Available'] = False
            books.append(book)
        return books

    def get_books_for_employee(self):
        db_books = self.repository.get_all()
        books = []
        for db_book in db_books:
            if any(x['Id'] == db_book['book_id'] for x in books):
                continue
            book = {
                'Id': db_book['book_id'],
                'Title': db_book['title'],
                'Pages': db_book['pages'],
                'ValueMulct': db_book['value_mulct'],
                'Publisher': db_book['publisher_name'],
                'Quantity': db_book['quantity'],
                'Genres': '',
                'Authors': '',
                'Loaded': 0,
                'Available': db_book['quantity'],
            }
            if db_book['collection_id']:
                book['Collection'] = db_book['collection_name']
            books_by_book_id = list(filter(lambda x: x['book_id'] == db_book['book_id'], db_books))

            mapped_list = list(
                map(lambda x: x['genre_description'], books_by_book_id))
            for genre in mapped_list:
                if genre in book['Genres']:
                    continue
                if not book['Genres']:
                    book['Genres'] = genre
                    continue
                book['Genres'] += f', {genre}'

            mapped_list = list(
                map(lambda x: x['author_name'], books_by_book_id))
            for author in mapped_list:
                if author in book['Authors']:
                    continue
                if not book['Authors']:
                    book['Authors'] = author
                    continue
                book['Authors'] += f', {author}'

            loans = self.repository.get_count_loans(book['Id'])

            book['Loaded'] = loans
            book['Available'] -= loans

            books.append(book)
        return books

    def get(self, book_id):
        db_books = self.repository.get(book_id)
        books = []
        for db_book in db_books:
            if any(x['Id'] == db_book['book_id'] for x in books):
                continue
            book = {
                'Id': db_book['book_id'],
                'Title': db_book['title'],
                'Description': db_book['description'],
                'ValueMulct': db_book['value_mulct'],
                'Publisher': db_book['publisher_name'],
                'Images': [],
                'Genres': '',
                'Authors': '',
            }
            if db_book['collection_id']:
                book['Collection'] = db_book['collection_name']
            books_by_book_id = list(filter(lambda x: x['book_id'] == db_book['book_id'], db_books))

            mapped_list = list(
                map(lambda x: f"{x['content_type']},{x['image']}", books_by_book_id))
            for image in mapped_list:
                if any(x == image for x in book['Images']):
                    continue
                book['Images'].append(image)

            mapped_list = list(
                map(lambda x: x['genre_description'], books_by_book_id))
            for genre in mapped_list:
                if genre in book['Genres']:
                    continue
                if not book['Genres']:
                    book['Genres'] = genre
                    continue
                book['Genres'] += f', {genre}'

            mapped_list = list(
                map(lambda x: x['author_name'], books_by_book_id))
            for author in mapped_list:
                if author in book['Authors']:
                    continue
                if not book['Authors']:
                    book['Authors'] = author
                    continue
                book['Authors'] += f', {author}'

            books.append(book)
        return books[0]

    def insert(self, book):
        try:
            # self.validate(book)
            # if not hasattr(book.collection, 'id'):
            #     from src.model.Collection import Collection
            #     book.collection = Collection(0, '')
            return self.repository.insert(book)
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
            # self.validate(book)
            return self.repository.update(book)
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
