import json
from flask import request

from src.model.Book import Book
from src.model.Collection import Collection
from src.model.Genre import Genre
from src.model.Publisher import Publisher

service = {}
app = {}


class BookController:

    def __init__(self, _service, _app):
        global app
        global service
        app = _app
        service = _service

        @app.route("/book")
        def get_books():
            json_return = json.dumps(service.get_all(), default=object_dict)
            return json_return

        @app.route("/book/<book_id>")
        def get_book(book_id):
            json_return = json.dumps(service.get(book_id), default=object_dict)
            return json_return

        @app.route("/book", methods=['POST'])
        def insert_book():
            try:
                book = Book(
                    0,
                    request.json['title'],
                    request.json['pages'],
                    request.json['value_mulct']
                )
                book.publisher = Publisher(
                    request.json['publisher'],
                    '',
                )
                if 'collection' in request.json:
                    book.collection = Collection(
                        request.json['collection'],
                        '',
                    )
                book.genre = Genre(
                    request.json['genre'],
                    '',
                )
                return service.insert(book)
            except Exception as e:
                return 'json invalido'

        @app.route("/book", methods=['PUT'])
        def update_book():
            try:
                book = Book(
                    request.json['id'],
                    request.json['title'],
                    request.json['pages'],
                    request.json['value_mulct']
                )
                book.publisher = Publisher(
                    request.json['publisher'],
                    '',
                )
                if 'collection' in request.json:
                    book.collection = Collection(
                        request.json['collection'],
                        '',
                    )
                book.genre = Genre(
                    request.json['genre'],
                    '',
                )
                return service.update(book)
            except Exception as e:
                return 'json invalido'

        @app.route("/book/<book_id>", methods=['DELETE'])
        def delete_book(book_id):
            return service.delete(book_id)

        def object_dict(obj):
            return obj.__dict__
