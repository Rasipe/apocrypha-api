import json
from flask import request

from src.model.Book import Book
from src.model.Collection import Collection
from src.model.Genre import Genre
from src.model.Publisher import Publisher

from src.services import book_service as service
from src.util.Util import object_dict


def get_books():
    json_return = json.dumps(service.get_all(), default=object_dict)
    return json_return


def get_book(book_id):
    json_return = json.dumps(service.get(book_id), default=object_dict)
    return json_return


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
    except KeyError as e:
        return 'json invalido'


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
    except KeyError as e:
        return 'json invalido'


def delete_book(book_id):
    return service.delete(book_id)
