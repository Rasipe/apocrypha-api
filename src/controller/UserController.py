import json
from flask import request
from src.services import user_service as service
from src.util.Util import object_dict
from src.model.User import User


def get_users():
    json_return = json.dumps(service.get_all(), default=object_dict)
    return json_return


def insert_user():
    try:
        user = User(
            0,
            f'{request.json["name"]} {request.json["surname"]}',
            request.json['phone'],
            request.json['email']
        )
        return service.insert(user)
    except KeyError as e:
        return 'json invalido'


def update_user():
    try:
        user = User(
            request.json["id"],
            f'{request.json["name"]} {request.json["surname"]}',
            request.json['phone'],
            request.json['email']
        )
        return service.update(user)
    except KeyError as e:
        return 'json invalido'

def delete_user(user_id):
    return service.delete(user_id)
