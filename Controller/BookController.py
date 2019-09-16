import json
from flask import request

from model.Book import Book
from model.Collection import Collection
from model.Genre import Genre
from model.Publisher import Publisher

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
                    request.json['publisher']['id'],
                    request.json['publisher']['name'],
                )
                if 'collection' in request.json:
                    book.collection = Collection(
                        request.json['collection']['id'],
                        request.json['collection']['name'],
                    )
                book.genre = Genre(
                    request.json['genre']['id'],
                    request.json['genre']['description'],
                )
                return service.insert(book)
            except Exception as e:
                return 'json invalido'

        def object_dict(obj):
            return obj.__dict__
