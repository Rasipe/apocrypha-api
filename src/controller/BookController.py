import json
from flask import request
from src.services import book_service as service
import ast


def get_books_for_client():
    json_return = json.dumps(service.get_books_for_client())
    return json_return


def get_books_for_employee():
    json_return = json.dumps(service.get_books_for_employee())
    return json_return


def get_book(book_id):
    json_return = json.dumps(service.get(book_id))
    return json_return


def insert_book():
    try:
        return service.insert(request.json)
    except KeyError as e:
        return 'json invalido'


def update_book():
    try:
        return service.update(request.json)
    except KeyError as e:
        return 'json invalido'


def delete_book(book_id):
    return service.delete(book_id)
